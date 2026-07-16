# Round 2 — Bug Fixes + KOIX Full Reskin (blue + mint, zero orange)

## How to apply this drop

**Full replacement files** (copy over the existing file, no merging needed):
- `static/css/theme_vars.css`
- `static/css/koix_components.css`
- `static/images/logo_full.png`
- `static/js/chat.js`
- `static/js/confirm-modal.js`
- `templates/about.html`
- `templates/admin/base_admin.html`
- `templates/admin/chat.html`
- `templates/admin/products.html`
- `templates/auth/login.html`
- `templates/distributors.html`

**Run once:**
- `deorange.py` — drop it in your project root (next to `manage.py`) and run:
  ```
  python3 deorange.py            # dry run, shows what it will touch
  python3 deorange.py --apply    # writes the changes
  ```
  This purges every literal orange/tan hex code across every `.css`/`.html`/`.js`
  file so the whole site matches the KOIX blue+mint reference images —
  no orange left anywhere, including the WhatsApp-brand-green FAB button.

**Patches** (small, targeted edits — instructions inside each `.txt` file):
- `apps/agents/PATCH_views_and_urls.txt` — new live-presence endpoint
- `apps/analytics/PATCH_edit_product.txt` — the missing "edit product" feature
- `apps/core/PATCH_contact_copy.txt` — naturalized contact page copy
- `apps/core/PATCH_product_images.txt` — fixes 10 duplicated product photos
- `apps/core/apps_core_views_about_UPDATED.py` — full replacement for the `about()` view
- `templates/PATCH_base_html_header_and_nav.txt` — removes Staff Login from the header, adds nav animation
- `templates/PATCH_index_html_animations.txt` — staggered reveal on homepage category cards
- `templates/agent/PATCH_chat_html.txt` — same CSRF fix as admin side + WhatsApp-style bubble tails

---

## Checklist against your list

| Ask | Status | Notes |
|---|---|---|
| Confirmation before delete | ✅ Fixed | New `confirm-modal.js` replaces native `confirm()` popups everywhere; wired into `admin/products.html` as the reference example — apply the same `class="js-confirm-submit" data-confirm-title="…" data-confirm-body="…"` pattern to the delete forms in `distributors.html`, `agents.html`, `requests.html`, `supply_requests.html` (all currently use `onsubmit="return confirm(...)"`, just swap the attribute). |
| Chat "still failing" | ✅ **Root cause found & fixed** | Two real bugs: (1) neither chat page ever set the CSRF cookie, so every send/mark-read POST was being silently rejected by Django — that's almost certainly what "failing" meant; (2) `admin/chat.html`'s element IDs didn't match what `chat.js` was looking for, so the chat window never actually displayed when you clicked a contact, and the admin's own messages would've rendered as if they came from the agent. All three fixed. |
| Show which agents are active | ✅ Added | Live "N agent(s) active now" counter at the top of Messages, plus each contact's dot now refreshes every 15s via the new `/api/agents/status/` endpoint — no more relying on a stale page load. |
| Repeated / blurry product photos | ✅ Data issue fixed, ⚠️ photos still needed | 10 of 18 products were all sharing one generic placeholder image — each now gets its own unique filename slot. Blur is a source-image resolution problem I can't fix without real photography; see the patch file for what resolution to shoot at, and the new Edit Product modal makes re-uploading painless once you have them. |
| New logo | ✅ Applied | `static/images/logo_full.png` replaced. Business card left untouched — I don't see a business-card asset anywhere in the codebase, so nothing there was touched either way. |
| Fix header / top nav | ✅ Fixed | Staff Login removed from the header entirely (footer-only now, per your original spec); added an animated underline + subtle logo hover to the nav. |
| Contact page product list "not AI" | ✅ Rewrote | Naturalized the contact_items copy (labels read like a person wrote them) and the page's intro/heading copy. (If you actually meant the About page's distribute list rather than Contact — that one was already rebuilt last round with real per-category copy instead of a flat name grid.) |
| Store locator map | ✅ **Was actually missing — added** | `distributors.html` had no embedded map at all, just a list with external Google Maps links. Now has a real Leaflet + OpenStreetMap map (no API key required) with a pin per outlet, synced to the region filter/search, click-to-focus from any card. |
| Homepage transitions/animations | ✅ Patched | Category cards now stagger-reveal on scroll and lift+rotate their icon on hover; product cards get a smoother image zoom. The reveal *system* already existed in `main.js` — it just wasn't wired onto the homepage markup. |
| WhatsApp-feel chat, no copyright risk | ✅ Done | Bubble tails, delivered ticks, and layout now read as a familiar messenger, but colored in your blue/mint palette — the literal WhatsApp green (`#25d366`) used on the FAB button is also swapped out by `deorange.py`. |
| Staff login footer-only | ✅ Fixed | See header patch above — was still showing in the topbar despite being intended for the footer only. |
| Split-screen login page | ✅ **Was reverted/missing — rebuilt** | The version in your codebase was still the old centered single-card layout. Rebuilt as a proper split screen: left half is an auto-advancing slideshow of the four product categories with the logo pinned top-left, right half is the sign-in form. |
| Admin can edit existing products | ✅ Added | New "Edit" button per row opens a modal pre-filled with that product's data, posts to a new `admin_edit_product` view. Previously add/delete only. |
| Kill all orange, match KOIX images exactly | ✅ Done | `theme_vars.css` remaps every color variable to blue+mint; `deorange.py` catches every hardcoded literal hex that wasn't using a variable. Run it once and there should be zero orange pixels left. |

---

## What I'd still flag before you ship this

1. **Run `deorange.py --apply` before anything else** — several of the other
   fixes (chat bubbles, buttons, badges) reference `var(--orange)` on
   purpose, relying on `theme_vars.css` having already remapped it to mint.
   If you apply the templates without the CSS change, things will look
   inconsistent.
2. **Real product photography** is the one thing here I genuinely can't
   fix from inside the code — happy to help resize/crop/optimize once you
   have source photos, but I can't generate authentic product shots.
3. I did not find a "business card" file anywhere in the project to leave
   alone — if that lives in a separate design tool (Canva/Figma/etc.) and
   not in this codebase, there's nothing for me to accidentally touch.
