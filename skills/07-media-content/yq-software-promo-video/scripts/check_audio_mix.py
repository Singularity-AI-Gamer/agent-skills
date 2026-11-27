#!/usr/bin/env python3
"""Verify speech-to-BGM loudness balance and detect midrange bandstop hollowing."""

from __future__ import annotations

import argparse
import json
import sys
import wave
from pathlib import Path
import numpy as np


def read_wav_float(path: Path) -> tuple[int, np.ndarray]:
    with wave.open(str(path), "rb") as w:
        sr = w.getframerate()
        ch = w.getnchannels()
        sw = w.getsampwidth()
        raw = w.readframes(w.getnframes())
    if sw != 2:
        raise ValueError(f"Expected 16-bit PCM WAV for {path}, got {sw * 8}-bit")
    arr = np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0
    if ch > 1:
        arr = arr.reshape(-1, ch)
    else:
        arr = arr[:, None]
    return sr, arr


def check_mix(
    voice_path: Path,
    music_path: Path,
    min_diff_db: float = -8.5,
    max_diff_db: float = -7.0,
    min_mid_ratio: float = 0.08,
) -> dict:
    sr_v, voice = read_wav_float(voice_path)
    sr_m, music = read_wav_float(music_path)
    if sr_v != sr_m:
        raise ValueError(f"Sample rate mismatch: voice={sr_v}, music={sr_m}")

    n = min(len(voice), len(music))
    voice_m = voice[:n].mean(axis=1)
    music_m = music[:n].mean(axis=1)

    hop = max(1, int(0.01 * sr_v))
    blocks = n // hop
    v_rms_blk = np.sqrt(np.mean(voice_m[: blocks * hop].reshape(-1, hop) ** 2, axis=1))
    active_blk = v_rms_blk > max(0.01, float(np.max(v_rms_blk)) * 0.08)
    if not np.any(active_blk):
        raise ValueError("No active speech detected in voice WAV")

    active_samples = np.repeat(active_blk, hop)
    v_rms = float(np.sqrt(np.mean(voice_m[: blocks * hop][active_samples] ** 2)))
    m_rms = float(np.sqrt(np.mean(music_m[: blocks * hop][active_samples] ** 2)))
    diff_db = 20.0 * np.log10(max(m_rms, 1e-9) / max(v_rms, 1e-9))

    # Check midrange energy (500-2800 Hz) in music to catch accidental bandstop hollowing.
    fft_mag = np.abs(np.fft.rfft(music_m))
    freqs = np.fft.rfftfreq(len(music_m), d=1.0 / sr_v)
    total_e = float(np.sum(fft_mag ** 2)) + 1e-12
    mid_mask = (freqs >= 500.0) & (freqs <= 2800.0)
    mid_ratio = float(np.sum(fft_mag[mid_mask] ** 2)) / total_e

    passed = (min_diff_db <= diff_db <= max_diff_db) and (mid_ratio >= min_mid_ratio)
    return {
        "passed": bool(passed),
        "speech_active_rms_db": round(20.0 * np.log10(max(v_rms, 1e-9)), 2),
        "music_under_speech_rms_db": round(20.0 * np.log10(max(m_rms, 1e-9)), 2),
        "music_minus_speech_db": round(diff_db, 2),
        "target_range_db": [min_diff_db, max_diff_db],
        "music_midband_500_2800hz_ratio": round(mid_ratio, 4),
        "min_midband_ratio": min_mid_ratio,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate TTS and BGM mix balance and midrange presence.")
    parser.add_argument("--voice", required=True, type=Path, help="Speech-only WAV (centered/normalized)")
    parser.add_argument("--music", required=True, type=Path, help="Ducked BGM-only stem WAV")
    parser.add_argument("--min-db", type=float, default=-8.5, help="Minimum BGM-minus-speech dB")
    parser.add_argument("--max-db", type=float, default=-7.0, help="Maximum BGM-minus-speech dB")
    args = parser.parse_args()

    report = check_mix(args.voice, args.music, args.min_db, args.max_db)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
