# KOIX-Style Reskin — Blue + Mint Green

## What's in this drop

1. **`static/css/theme_vars.css`** — replaces your current file. Same variable
   *names* as before (so nothing else breaks), but the values now point to
   blue + mint green instead of blue + orange/cosmos. Light/dark mode still
   works exactly as before — it's all driven by `[data-theme="dark"]`, untouched.

2. **`static/css/koix_components.css`** — new file. This is the reusable
   component system: the dark hero panel (`.koix-hero`), the icon-badge
   cards (`.icon-card`), pill buttons (`.btn-mint`, `.btn-blue`), the tag/
   section-title pair (`.koix-tag` / `.koix-section-title`), and product
   chips (`.chip`). Link it in `base.html` right after `theme_vars.css`:

   ```html
   <link rel="stylesheet" href="{% static 'css/theme_vars.css' %}">
   <link rel="stylesheet" href="{% static 'css/koix_components.css' %}">
   ```

3. **Fonts** — swapped Playfair Display + DM Sans for **Plus Jakarta Sans**
   (headings) + **Lato** (body), per your spec doc's "Friendly Tech" combo —
   distinct enough for the homepage, clean and human everywhere else. Add
   this to `<head>` in `base.html` in place of the old Google Fonts line:

   ```html
   <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Lato:wght@400;600;700&display=swap" rel="stylesheet">
   ```

4. **`templates/about.html`** — fully rebuilt. The old "What We Distribute"
   section (18 flat colored boxes, just a product name + category) is gone.
   It's now 4 icon-cards, one per category, each with:
   - a mint icon badge (bug / seedling / microscope / boxes)
   - a genuinely written one-line description of what that category solves
     for a farmer, instead of just repeating the product name
   - a row of chips listing the real product names underneath

5. **`apps_core_views_about_UPDATED.py`** — the matching view. It replaces
   the flat `product_samples` list with `product_groups`, grouped by
   category with the icon + blurb + item list. Copy this into
   `apps/core/views.py`, replacing the existing `about()` function.

## Why this fixes the "mechanical" feeling

The old section had zero hierarchy — 18 identically-shaped boxes, each just
a bolded product code and a lowercase category tag. There was no read on
*why* a product matters, so it reads like a database dump. The new version
groups by the actual decision a farmer makes ("I have an insect problem" →
Pesticides), gives one warm sentence of context, and only then shows the
specific product names as secondary detail (chips). That's the same
information hierarchy KOIX uses in the "What Benefits You Will Get" grid.

## Rolling this out to the rest of the site

Right now only `about.html` uses the new components. To carry the KOIX look
through the rest of the site, the pattern to repeat is:

- Replace ad-hoc inline-styled boxes with `<div class="icon-card">` +
  `.icon-badge` wherever you have a features/benefits/why-us grid
  (`index.html`'s "Why Choose Us" section, the product detail page's
  safety notice, the agent dashboard KPI tiles).
- Replace the space/cosmos hero backgrounds (`.hero`, `.page-hero` in
  `style.css` / `theme.css`) with `.koix-hero` for a consistent dark panel
  across every page-hero.
- Swap `btn-green` usages for `.btn-mint`, and `btn-secondary` for
  `.btn-blue` — I kept the old class names working as aliases so nothing
  breaks immediately, but new markup should use the new names directly.

Given the number of templates (30+), I focused this pass on: the design
token foundation, the reusable component library, and the one section you
specifically flagged as broken. Say the word and I'll go template-by-
template next (start with `index.html` and `product_detail.html`, since
those get the most traffic).
