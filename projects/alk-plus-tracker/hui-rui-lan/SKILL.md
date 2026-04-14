---
name: hui-rui-lan
description: 重建或扩展 ALK+ Tracker UI 时使用，要求保留原始品牌蓝视觉系统、区块顺序、玻璃卡片布局，而不是重新设计页面。
---

# Brand Blue

This skill locks the UI to the original downloaded `ALK+ Lung Cancer Treatment Tracker` page. It is not a loose inspiration board. It is a page-level constraint set.

Reference files:
- The downloaded HTML snapshot in the repo root
- The downloaded asset directory HTML entry file
- The bundled CSS file in the asset directory (`index-*.css`)
- User-provided full-page screenshots at 50% zoom

## Non-Negotiables

- Do not replace the cool brand-blue palette with red, purple, black-gold, Apple glass, or generic SaaS blue-white styling.
- Do not reorder, merge, remove, or rename top-level sections unless the user explicitly asks.
- Do not change the page density model. The page is a narrow centered content column with large white margins and thin glass cards.
- Do not move core interaction zones. Search, the blue intelligence banner, the filter bar, and the timeline feed must stay.
- Do not render implementation notes, rewrite notes, TODOs, or scope commentary in visible UI text.

## Source Tokens

These values come directly from the original CSS and should be treated as the source of truth:

- `--radius: 0.5rem`
- `--background: oklch(98% .01 264)`
- `--foreground: oklch(20% .1 264)`
- `--card: oklch(100% 0 0)`
- `--card-foreground: oklch(20% .1 264)`
- `--primary: oklch(45% .26 264)`
- `--primary-foreground: oklch(100% 0 0)`
- `--secondary: oklch(95% .04 264)`
- `--secondary-foreground: oklch(30% .15 264)`
- `--muted: oklch(96% .02 264)`
- `--muted-foreground: oklch(55% .1 264)`
- `--accent: oklch(93% .06 264)`
- `--accent-foreground: oklch(35% .2 264)`
- `--border: oklch(90% .05 264)`
- `--input: oklch(90% .05 264)`
- `--ring: oklch(45% .26 264)`

Implementation intent:

- The page background is a very pale blue-white, not plain white.
- Titles and body text are navy-blue biased, not black.
- The entire emphasis system is driven by `--primary`.
- Support colors may exist only as pale local tints. They must never overpower the blue system.

## Component Rules

### 1. Glass Card

All general cards should inherit the original `.glass-card` behavior:

- `border: 1px solid color-mix(in oklab, var(--primary) 10%, transparent)`
- `background: #ffffffb3`
- If `color-mix` is available, this is effectively `white 70% + transparent`
- `box-shadow: 0 1px 3px 0 rgba(0,0,0,.10), 0 1px 2px -1px rgba(0,0,0,.10)`
- `backdrop-blur: 24px`
- On hover, the border rises to `primary 30%` and the shadow increases slightly

Do not invent a second material system.

### 2. Hero Glow

The hero title keeps a soft blue glow:

- `text-shadow: 0 0 30px oklch(45% .26 264 / 0.3)`

Do not replace this with a heavy dark shadow.

### 3. Scrollbar

- Thumb uses translucent primary
- Hover only slightly increases intensity
- Do not switch to gray system scrollbars

### 4. Border and Radius

- Use `0.5rem` as the page-wide corner rule
- Borders stay thin and light
- Avoid thick outlines, heavy shadows, and oversized radius values

## Fixed Page Map

Keep this section order:

1. Top navigation
2. Hero
3. Search
4. `Lorlatinib Market Intelligence` blue banner
5. `Subtype Deep Dive`
6. `Sequencing Strategy`
7. `Tailwinds (Pros)`
8. `Headwinds (Cons)`
9. `SWOT`
10. `Key Promotion Points`
11. `Customer Segmentation & Strategy Matrix`
12. Filter bar
13. Timeline-style `Latest Updates / Competitive Intelligence` feed

## Section-Specific Constraints

### Hero

- Narrow centered content column
- Large pale biotech-style backdrop with generous whitespace
- Two-line headline with stronger second-line brightness
- One short supporting line below
- Search box floats below the hero copy

### Blue Intelligence Banner

- Deep-blue to bright-blue horizontal gradient
- White text
- Small badge at the upper left
- Low-contrast decorative motif on the right
- This is the main business banner and must not collapse into a plain white card

### Subtype Deep Dive / Sequencing Strategy

- Two-column layout
- Left side contains subtype or scenario cards
- Right side contains sequencing comparison cards
- Each inner card uses thin borders and pale surfaces
- Metrics, labels, and comparison boxes must remain visually separated inside the card

### Tailwinds / Headwinds

- Left column uses pale green cards for pros
- Right column uses pale pink or pale red cards for cons
- These are local emotional tints only, not page-level palette changes
- Small impact pills remain at the upper right of cards

### SWOT

- Four narrow parallel cards
- Colors remain pale blue, pale yellow, pale green, and pale gray
- Title height should align across the row
- Content stays short and list-like, not essay-style

### Key Promotion Points

- Multiple compact message cards in a dense grid
- Each card keeps a small audience or category label at the top
- Main message sits in the center
- Source line remains at the bottom

### Customer Segmentation & Strategy Matrix

- Title row first
- Multiple persona strategy cards below
- Each card must preserve these stacked layers:
  - persona title
  - short persona descriptor
  - core needs
  - strategy
  - key message
  - action item

Do not flatten these into plain paragraphs.

### Filter Bar

- One standalone white or glass-like horizontal container
- Left side contains category, CN status, and therapy controls
- Right side displays update count
- Filter chips stay thin, light, and low-weight
- Therapy dropdown remains visible

### Timeline Feed

- Vertical timeline layout
- Blue dot and fine vertical line on the left
- White glass card on the right
- Top metadata row contains status, type, date, and source
- Headline is bold navy
- Summary is lighter and quieter
- Tag pills remain at the bottom

## Layout and Whitespace

- This is not a full-width dashboard.
- Keep substantial left and right margins so the page reads as a centered intelligence sheet.
- The hero-to-banner rhythm stays spacious.
- Lower card groups are dense but still separated by consistent small gaps.
- Do not stretch the interface into a wide grid.

## Copy Rules

- Headlines should be short, hard, and business-facing.
- Summaries should usually stay within 2 to 4 lines.
- Strategy copy can be full-sentence, but it must read like a business action, not a UI explanation.
- Never render phrases like `keep the old layout`, `content only`, `replica in progress`, `implementation note`, or similar developer-facing language.

## How To Apply This Skill

When editing this project:

1. Compare against the original page and screenshots first.
2. If the new output looks like a different product, roll it back and move it closer to this system.
3. Reuse the original tokens, borders, blur, and pale-support-color logic before creating anything new.
4. By default, only the content layer is meant to change:
   - strengths and weaknesses
   - SWOT
   - positioning
   - customer personas
   - key messages
   - competitive intelligence updates

## Final Audit

- Is blue still the only dominant color family?
- Is the top-level section order still intact?
- Are the filter bar and timeline still in their original roles and positions?
- Do cards still read as thin-border glass cards instead of heavy solid blocks?
- Did any developer-facing text leak into the UI?
- Does the page still read immediately as the same product shown in the reference screenshots?
