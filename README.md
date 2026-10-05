# East Side Ballas (ESB)

Initial website foundation for the East Side Ballas GTA V roleplay community. The repository previously contained only `.gitkeep`; this starter establishes real public pages without assuming a backend or working integrations.

## Structure and approach

Use dependency-free, multi-page HTML with shared CSS and a small progressive-enhancement script. This keeps the first version easy to inspect, edit, serve, and migrate to a server framework when authentication and persistence requirements are agreed.

```text
index.html             Home and family values
about.html             Public ESB introduction
members.html           Empty state for approved member profiles
announcements.html     Empty state for confirmed updates
applications.html      Joining information; no data collection
admin.html             Public implementation-status page only
assets/styles.css      Responsive design and brand tokens
assets/site.js         Footer year enhancement
scripts/check.py       Local asset, navigation, and HTML checks
docs/ROADMAP.md         Scope, integration decisions, and next steps
```

## Run locally

From the repository root, with Python 3 installed:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://localhost:8000. No package installation, build step, environment variables, or credentials are needed. Static hosting can serve the repository files directly; no hosting provider or automatic deployment has been configured.

## Validate

```sh
python3 scripts/check.py
node --check assets/site.js
```

The Python check verifies local links/assets, unique IDs, document language, titles, main landmarks, and current-page navigation on public pages. Browser visual and keyboard review should follow before a public release.

## Scope and current status

- Implemented: purple/black responsive layout, official primary color `#36013F`, public navigation, introductory copy, skip link, keyboard focus styles, and honest empty states.
- Planned: approved member photos/social profiles, announcements, application submission, Discord login, and protected admin management.
- Not implemented: OAuth, sessions, Discord roles/member counts, webhooks, database, uploads, application forms, or admin operations. The login button is disabled and visibly labeled coming soon. `admin.html` is public and must never hold private records.

No roster, statistics, meeting dates, social URLs, or Discord invite have been invented. Add those only after confirmation. The ESB monogram is text, not an official supplied logo.

## Editing

Edit content in the corresponding HTML page. Keep shared header/footer changes consistent across all six pages. Update design tokens in `assets/styles.css`; keep readable accents separate from the deep purple brand color. The website works without JavaScript.

Never place Discord client secrets, bot tokens, webhook URLs, or private member information in public HTML, browser scripts, or commits. See [the roadmap](docs/ROADMAP.md) for the backend boundary and acceptance criteria.
