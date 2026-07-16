# Round 3 — Grayscale + Glow Theme, Product Grid Fix

## Files in this drop (full replacements)
- `static/css/theme_vars.css` — v7. Base is grayscale/white only. The two
  only colors anywhere on the site now are light blue (`--accent-blue`)
  and red (`--accent-red`), and both are used exclusively as glow accents
  (a soft `box-shadow`), never as a solid fill covering large areas.
- `static/css/koix_components.css` — v2, rebuilt against the new tokens.
  New `.product-photo-grid` / `.product-photo-card` component added
  specifically for the fix below.
- `templates/about.html` — full rebuild of "What We Distribute."
- `apps/core/views_about_UPDATED.py` — replace your `about()` view with
  this. Copy/paste into `apps/core/views.py`.
- `finalize_grayscale_theme.py` — run this once in your project root
  (**instead of** the earlier `deorange.py` — this one is a superset that
  also removes the mint/green from last round and the original dark-green
  hero/footer backgrounds):
  ```
  python3 finalize_grayscale_theme.py            # dry run
  python3 finalize_grayscale_theme.py --apply    # writes changes
  ```

## 1. "What We Distribute" — corrected

Last round I misread this as "the section looks bad" and replaced the
per-product listing with category summary cards + a text chip list. That
was wrong — you wanted every product kept, just presented properly. Fixed:

- The view now pulls **actual `Product` rows from the database**, grouped
  by category, instead of a hardcoded name list. Add or edit a product in
  the admin and it appears here automatically with whatever photo is on
  that product record — no template edits ever needed again for this.
- Each product renders as its own card: **photo on top, name below**, in
  a clean grid under its category header (Pesticides / Herbicides /
  Fungicides / Fertilizers & Equipment) — matching exactly what you asked
  for the second time around.
- Category headers still carry one line of real context (not filler
  copy), but every individual product is visible and clickable through to
  its detail page.

## 2. Header vs. footer — confirmed, not changed further

Re-checking your description against what's already in place from last
round:
- **Header/topbar**: phone, email, hours, Facebook — contact details only.
- **Footer**: Staff Login link, plus the rest of the site links (Products,
  Company, Contact, etc.)

This already matches "contact details in the header, admin logins and
others in the footer" — so no new file needed here. If anything still
looks off once you're looking at it live, tell me exactly what you're
seeing (a screenshot helps) and I'll fix the specific spot rather than
guess again.

## 3. The actual color system now

Only two accent colors exist anywhere: light blue and red. Neither is
used as a large background fill — they show up as:
- A 1.5px colored border + soft glow (`box-shadow`) on primary buttons
- The same glow on an active tab/pill
- A thin glow ring around icon badges so they're still easy to spot on
  an all-gray card
- Red is reserved for anything that should draw the eye as "pay attention
  here" (delete buttons, low-stock badges) — blue is the general
  interactive/primary accent everywhere else

Everything else — cards, backgrounds, borders, body text — is pure
grayscale or white, including in dark mode (which now goes to near-black
grays instead of the old very-dark-green/navy).

## Order to apply things

1. Run `finalize_grayscale_theme.py --apply` first.
2. Then drop in the two CSS files (they'll already match what the script
   just did, no conflict).
3. Then the `about.html` + view change.
4. Everything from Round 2 (chat fixes, map, edit-product modal, split
   login, confirm-modal, logo) is unaffected by this and still applies on
   top — this round only touches color tokens and the distribute section.
