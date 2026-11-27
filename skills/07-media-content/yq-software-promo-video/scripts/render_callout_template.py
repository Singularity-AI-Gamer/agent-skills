#!/usr/bin/env python3
"""Reusable Pillow compositing primitives for 45s software promo videos.

Provides:
- Full-window paper-framed hero display (`draw_full_window`)
- Animated highlight outline (`draw_animated_outline`)
- Two-stage full-window locator + pop-out zoomed callout (`render_feature_callout`)
- Four platform safe-zone covers (`render_platform_covers`)
"""

from __future__ import annotations

import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

CREAM = "#fff0ce"
INK = "#183a3a"
RED = "#be4435"
TEAL = "#176658"
GOLD = "#ecbb61"


def ease(x: float) -> float:
    x = max(0.0, min(1.0, x))
    return x * x * (3.0 - 2.0 * x)


def phase(t: float, a: float, b: float) -> float:
    return ease((t - a) / max(1e-6, b - a))


def paper_band(im: Image.Image, x: float, y: float, w: float, h: float, color: str) -> None:
    x, y, w, h = map(int, (x, y, w, h))
    pts = [(x + 2, y + 3), (x + w - 11, y), (x + w, y + 5), (x + w - 3, y + h - 3), (x + 8, y + h), (x, y + h - 5)]
    draw = ImageDraw.Draw(im)
    draw.polygon([(px + 4, py + 5) for px, py in pts], fill="#695541")
    draw.polygon(pts, fill=color)


def draw_full_window(
    canvas: Image.Image,
    ui_img: Image.Image,
    x: int,
    y: int,
    target_w: int,
    dim: float = 0.0,
    blur_blend: float = 0.0,
) -> tuple[int, int]:
    resized = ui_img.convert("RGB").resize(
        (target_w, round(target_w * ui_img.height / ui_img.width)),
        Image.Resampling.LANCZOS,
    )
    if blur_blend > 0:
        resized = Image.blend(resized, resized.filter(ImageFilter.GaussianBlur(5)), blur_blend)
    if dim > 0:
        resized = ImageEnhance.Brightness(resized).enhance(1.0 - dim)
    paper_band(canvas, x - 6, y - 7, resized.width + 12, resized.height + 14, CREAM)
    canvas.paste(resized, (x, y))
    return resized.size


def draw_animated_outline(
    canvas: Image.Image,
    rect: tuple[float, float, float, float],
    progress: float,
    color: str = RED,
    width: int = 5,
) -> None:
    x0, y0, x1, y1 = rect
    pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1), (x0, y0)]
    lengths = [math.dist(a, b) for a, b in zip(pts, pts[1:])]
    remaining = sum(lengths) * max(0.0, min(1.0, progress))
    draw = ImageDraw.Draw(canvas)
    for a, b, seg_len in zip(pts, pts[1:], lengths):
        k = max(0.0, min(1.0, remaining / max(1e-6, seg_len)))
        if k > 0:
            draw.line([a, (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)], fill=color, width=width)
        remaining -= seg_len


def render_feature_callout(
    canvas: Image.Image,
    full_ui: Image.Image,
    crop_box: tuple[int, int, int, int],
    locator_box: tuple[int, int, int, int],
    t: float,
    title: str,
    result_text: str,
    font_fn,
    callout_side: str = "right",
) -> None:
    """Render two-stage full-window locator + pop-out zoomed detail card."""
    w = 1120
    x, y = (canvas.width - w) // 2, 4
    s = w / full_ui.width
    u = phase(t, 0.32, 0.66)
    draw_full_window(canvas, full_ui, x, y, w, dim=0.18 * u)

    rect = (
        x + s * locator_box[0],
        y + s * locator_box[1],
        x + s * locator_box[2],
        y + s * locator_box[3],
    )
    draw_animated_outline(canvas, rect, phase(t, 0.0, 0.26))
    if t < 0.32:
        return

    src = full_ui.crop(crop_box)
    cw = round(784 * (0.15 + 0.85 * u))
    ch = round(cw * src.height / src.width)
    ax, ay = (rect[0] + rect[2]) / 2.0, (rect[1] + rect[3]) / 2.0
    target_left = 138 if callout_side == "left" else 355
    left = round((ax - cw / 2) * (1.0 - u) + target_left * u)
    top = min(round((ay - ch / 2) * (1.0 - u) + 215 * u), 590 - ch)

    draw = ImageDraw.Draw(canvas)
    for px, py, ex, ey in [(rect[0], rect[1], left, top), (rect[2], rect[3], left + cw, top + ch)]:
        draw.line((px, py, ex, ey), fill=CREAM, width=6)
        draw.line((px, py, ex, ey), fill=RED, width=2)
        draw.ellipse((px - 5, py - 5, px + 5, py + 5), fill=GOLD)

    shadow = Image.new("RGBA", (cw + 65, ch + 75))
    ImageDraw.Draw(shadow).rectangle((20, 23, cw + 32, ch + 37), fill=(30, 25, 20, 148))
    shadow = shadow.filter(ImageFilter.GaussianBlur(9))
    canvas.paste(shadow, (left - 20, top - 15), shadow)

    paper_band(canvas, left - 6, top - 7, cw + 12, ch + 14, CREAM)
    canvas.paste(src.resize((cw, ch), Image.Resampling.LANCZOS), (left, top))
    if u > 0.45:
        tw = int(font_fn(22).getlength(title)) + 34
        paper_band(canvas, left + 8, top - 46, tw, 44, INK)
        ImageDraw.Draw(canvas).text((left + 8 + tw / 2, top - 25), title, font=font_fn(22), fill="white", anchor="mm")
    if t > 0.66:
        z = phase(t, 0.66, 0.88)
        rw = int(font_fn(19).getlength(result_text)) + 34
        rx = left + 20 + int(30 * (1.0 - z))
        paper_band(canvas, rx, top + ch + 4, rw, 42, TEAL)
        ImageDraw.Draw(canvas).text((rx + rw / 2, top + ch + 24), result_text, font=font_fn(19), fill="white", anchor="mm")


def render_platform_covers(
    out_dir: Path,
    bg_landscape: Image.Image,
    home_ui: Image.Image,
    brand: str,
    hook_title: str,
    bili_title: str,
    xhs_title: str,
    zhihu_title: str,
    badge_text: str,
    font_fn,
) -> list[Path]:
    """Generate 4 platform safe-zone covers without hardcoded brand assets."""
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []

    # 1. Bilibili (avoid bottom-right duration badge)
    bi = ImageOps.fit(bg_landscape, (1280, 720)).convert("RGB")
    draw_full_window(bi, home_ui, 87, 10, 1106)
    paper_band(bi, 41, 116, 560, 212, INK)
    d = ImageDraw.Draw(bi)
    d.text((73, 175), bili_title, font=font_fn(40), fill=CREAM, anchor="lm")
    d.text((75, 268), brand, font=font_fn(52), fill=CREAM, anchor="lm")
    paper_band(bi, 61, 353, int(font_fn(28).getlength(badge_text)) + 36, 52, RED)
    d.text((79, 378), badge_text, font=font_fn(28), fill="white", anchor="lm")
    p_bi = out_dir / "cover_bilibili.jpg"
    bi.save(p_bi, quality=96)
    paths.append(p_bi)

    # 2. Douyin (keep text in upper-center 70%, avoid right & bottom)
    dy = ImageOps.fit(bg_landscape, (1280, 720)).convert("RGB")
    draw_full_window(dy, home_ui, 87, 10, 1106)
    paper_band(dy, 107, 76, 858, 121, INK)
    ImageDraw.Draw(dy).text((143, 134), hook_title, font=font_fn(54), fill=CREAM, anchor="lm")
    p_dy = out_dir / "cover_douyin.jpg"
    dy.save(p_dy, quality=96)
    paths.append(p_dy)

    # 3. Xiaohongshu 3:4 vertical
    xhs = ImageOps.fit(bg_landscape, (1080, 1440)).convert("RGB")
    paper_band(xhs, 41, 48, 999, 1240, CREAM)
    xd = ImageDraw.Draw(xhs)
    xd.text((90, 141), brand, font=font_fn(46), fill=TEAL, anchor="lm")
    xd.text((77, 277), xhs_title, font=font_fn(70), fill=INK, anchor="lm")
    draw_full_window(xhs, home_ui, 65, 493, 950)
    p_xhs = out_dir / "cover_xhs_3x4.jpg"
    xhs.save(p_xhs, quality=96)
    paths.append(p_xhs)

    # 4. Zhihu clean analytical style
    zh = ImageOps.fit(bg_landscape, (1280, 720)).convert("RGB")
    draw_full_window(zh, home_ui, 87, 10, 1106)
    paper_band(zh, 56, 120, 730, 182, CREAM)
    zd = ImageDraw.Draw(zh)
    zd.text((85, 180), zhihu_title, font=font_fn(35), fill=INK, anchor="lm")
    zd.text((86, 257), brand, font=font_fn(28), fill=TEAL, anchor="lm")
    p_zh = out_dir / "cover_zhihu.jpg"
    zh.save(p_zh, quality=96)
    paths.append(p_zh)

    return paths
