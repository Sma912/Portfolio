# Complete professional portfolio — ready for GitHub + Netlify

This folder is a **complete static website**. The home page is `index.html` in the repository root. It does not require npm, Node.js, Python, or any build process.

## Deploy via GitHub

1. In your GitHub `Portfolio` repository, upload **the contents of this ZIP into the root** of the `main` branch. Do not upload the ZIP as one file. `index.html` must be visible at the top level. Replace files when prompted. Remove old helper files (`PREVIEW_Writing_Portfolio.html`, `EMBED_IN_EXISTING_INDEX.html`, `merge_into_original.py`) if they remain from the previous add-on package; they are not part of this full website.
2. In Netlify: **Project configuration → Build & deploy / Continuous deployment** (label may vary). Choose `Sma912/Portfolio` and `main`. Leave **Base directory** and **Build command** empty. Set **Publish directory** to `.` (repository root).
3. Trigger a new production deploy, then open the root site and `/writing/`.
4. Review `sitemap.xml` and `robots.txt`.

### SEO note

Canonical and Open Graph URLs currently point to `https://sparkling-marzipan-d8432e.netlify.app` because this was the portfolio URL supplied. If you deploy to a **different Netlify domain** or connect your own domain, update absolute URLs in the HTML, `sitemap.xml`, and `robots.txt` before indexing it.

### Portfolio scope

The original website source was not available in the conversation. This is a newly built complete site using documented project names and existing writing samples; it is **not an exact visual or archival copy** of any older engineering gallery. Where no verified case study was available, project descriptions remain conservative.
