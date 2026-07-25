# Round 5 notes

## Real product photography
9 products now have real, correctly-cropped photos (up from 1 before this
round): MD Acelemectin, MD FOS 48EC, Muddosate, MD Top Laxlyn, Top-Laxly M,
MD Maize Plus, Max 2,4-D, MD Thoate, MD Thion — plus the two brand-new
products below. `reference_source_images/` holds the original flyer/photo
files you uploaded, kept only as a reference if you ever want a different
crop — this folder is **not** part of the served website (it sits outside
`static/`, so `collectstatic` never touches it).

Still on the generic fallback photo (no source image available yet):
MD Ametryn, Weed IT 75.7 XL, Top Fenos, Toplaxly 72WP (Cymoxanil), Copper
Oxychloride, Urea, NPK 17:17:17, Foliar Boost.

## Two new products added
- **M-D FOS 70SC** — dual-action Chlorpyrifos + Cypermethrin SC blend
- **MD BENZO-MECTIN 5WDG** — Emamectin Benzoate 5% WDG, for Fall Armyworm /
  Tuta Absoluta / Diamondback Moth
Both pulled from the spec sheet you uploaded, added in the same data
format and copy voice as every other product, with real cropped photos.

## Duplicate products — root cause fixed
`Product.name` had no uniqueness constraint, and the admin's "Add Product"
form never checked for an existing name before creating a new row — so
re-adding a product that was already seeded silently created a duplicate.
Fixed two ways:
1. `admin_add_product` now blocks a duplicate name (case-insensitive) and
   tells the admin to edit the existing product instead.
2. `python manage.py dedupe_products --apply` — a one-time cleanup command
   for any duplicates that already exist. It keeps whichever copy has a
   real photo (then longest description, then oldest), combines stock
   quantities from all copies into the kept one, and removes the rest.
   Run without `--apply` first to preview what it would do.

## Icons — Font Awesome removed entirely
Every icon on the site (nav, buttons, cards, admin sidebar — 65 distinct
icons, hundreds of instances) is now inline SVG via a custom `{% icon %}`
template tag (`apps/core/templatetags/icons.py`), not an icon font. This
is what was actually causing the "emoji-looking" icons — Font Awesome's
icon font renders via Unicode codepoints mapped to a webfont; if that font
fails to load (CDN blocked, slow, offline), browsers fall back to their
default font for those codepoints, which often means generic emoji-style
glyphs. Inline SVG has no such failure mode. The Font Awesome CDN `<link>`
tags have been removed from every template — the site no longer requests
that font at all.

A few spots swapped icons dynamically via JavaScript (theme light/dark
toggle, password show/hide, chat checkmarks, toast/newsletter icons) by
changing a CSS class — that approach doesn't work once icons aren't a
font, so those were rebuilt: the theme and password toggles now render
both icon states and use CSS to show/hide the right one (no JS-driven
markup swap at all), and the JS-generated ones (toasts, chat ticks) now
inject the SVG markup directly.
