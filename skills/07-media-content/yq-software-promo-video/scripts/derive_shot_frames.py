#!/usr/bin/env python3
"""Derive natural shot frame boundaries from a continuous narration WAV.

Finds low-RMS speech breath valleys near ideal shot durations instead of slicing
and time-warping each sentence independently.
"""

from __future__ import annotations

import argparse
import json
import wave
from pathlib import Path
import numpy as np


def load_mono_wav(path: Path) -> tuple[int, np.ndarray]:
    with wave.open(str(path), "rb") as w:
        sr = w.getframerate()
        ch = w.getnchannels()
        sw = w.getsampwidth()
        raw = w.readframes(w.getnframes())
    if sw != 2:
        raise ValueError(f"Expected 16-bit PCM WAV, got sample width {sw}")
    data = np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0
    if ch > 1:
        data = data.reshape(-1, ch).mean(axis=1)
    return sr, data


def find_valley_cuts(
    audio: np.ndarray,
    sr: int,
    num_shots: int,
    weights: list[float] | None = None,
    min_shot_s: float = 2.6,
    max_shot_s: float = 6.0,
    tail_hold_s: float = 0.85,
    fps: int = 12,
) -> dict:
    total_s = len(audio) / sr
    if weights is None:
        weights = [1.0] * num_shots
    if len(weights) != num_shots:
        raise ValueError("weights length must match num_shots")

    # Trim trailing silence for active speech end, then add controlled tail hold.
    hop = max(1, int(0.01 * sr))
    n_blocks = len(audio) // hop
    rms = np.sqrt(np.mean(audio[: n_blocks * hop].reshape(-1, hop) ** 2, axis=1))
    thresh = max(1e-4, float(np.percentile(rms, 95)) * 0.04)
    active = np.flatnonzero(rms > thresh)
    speech_end_s = min(total_s, (active[-1] + 5) * hop / sr) if len(active) else total_s
    final_duration_s = round((speech_end_s + tail_hold_s) * fps) / fps

    w_arr = np.asarray(weights, dtype=np.float64)
    cum_w = np.cumsum(w_arr[:-1]) / np.sum(w_arr)
    ideal_cuts = cum_w * speech_end_s

    cuts_s = [0.0]
    for target in ideal_cuts:
        lo_s = max(cuts_s[-1] + min_shot_s, target - 0.9)
        hi_s = min(speech_end_s - min_shot_s * (num_shots - len(cuts_s)), target + 0.9)
        if lo_s >= hi_s:
            chosen = max(cuts_s[-1] + min_shot_s, min(target, speech_end_s - 0.5))
        else:
            lo_b = max(0, int(lo_s / 0.01))
            hi_b = min(len(rms) - 1, int(hi_s / 0.01))
            window_rms = rms[lo_b : hi_b + 1]
            # Prefer quietest breath valley closest to the ideal point.
            scores = window_rms + 0.015 * np.abs(
                (np.arange(lo_b, hi_b + 1) * 0.01) - target
            )
            best_b = lo_b + int(np.argmin(scores))
            chosen = best_b * 0.01
        cuts_s.append(chosen)
    cuts_s.append(final_duration_s)

    frame_boundaries = [int(round(t * fps)) for t in cuts_s]
    durations = [
        round((b - a) / fps, 3)
        for a, b in zip(frame_boundaries, frame_boundaries[1:])
    ]
    for idx, dur in enumerate(durations, 1):
        if dur < min_shot_s * 0.85 or dur > max_shot_s * 1.15:
            raise ValueError(
                f"Shot {idx} duration {dur}s outside safe bounds [{min_shot_s}, {max_shot_s}]"
            )

    return {
        "fps": fps,
        "duration": round(frame_boundaries[-1] / fps, 3),
        "speech_end_s": round(speech_end_s, 3),
        "frame_boundaries": frame_boundaries,
        "shot_durations_s": durations,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Derive shot frame boundaries from continuous TTS WAV.")
    parser.add_argument("--wav", required=True, type=Path, help="Path to continuous mono/stereo PCM WAV")
    parser.add_argument("--shots", required=True, type=int, help="Number of shots")
    parser.add_argument("--fps", type=int, default=12, help="Video frame rate (default: 12)")
    parser.add_argument("--tail-hold", type=float, default=0.85, help="Music outro hold in seconds")
    parser.add_argument("--weights", type=str, default="", help="Comma-separated relative shot weights (e.g. text lengths)")
    parser.add_argument("--out", required=True, type=Path, help="Output timing.json path")
    args = parser.parse_args()

    weights = [float(x) for x in args.weights.split(",") if x.strip()] if args.weights else None
    sr, audio = load_mono_wav(args.wav)
    result = find_valley_cuts(
        audio=audio,
        sr=sr,
        num_shots=args.shots,
        weights=weights,
        tail_hold_s=args.tail_hold,
        fps=args.fps,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
