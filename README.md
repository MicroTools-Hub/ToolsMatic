# MicroTools

A fast, privacy-first bundle of 25 browser utilities. Everything runs locally, stays lightweight, and works offline-friendly thanks to the service worker. No logins, no uploads, just useful tools you can chain together.

## Highlights
- **Privacy-first**: all tools execute in-browser; no data leaves your device.
- **Offline-friendly**: pre-cached assets via the service worker (`sw.js`); update banner prompts when a new build is ready.
- **Piping between tools**: send text across Word Counter, Case Converter, Markdown Previewer, and Text Diff without copy/paste.
- **Keyboard shortcuts**: Ctrl/Cmd+Enter to trigger primary actions; Esc to clear memorable input (where applicable).
- **Consistent UI**: shared styling (`assets/styles.css`) and helpers (`assets/site.js`) for predictability.

## Tool Catalog (25)
- Text & writing: Word Counter, Case Converter, Lorem Ipsum Generator, Quote Generator, Text Diff Checker, Markdown Previewer, Regex Tester.
- Dev helpers: Password Generator, JWT Inspector, UUID Maker, Base64 Encoder, URL Encoder, JSON Formatter, HTML Minifier, Number Converter.
- Data & files: CSV Inspector, CSV to JSON, HTML Minifier, JSON Formatter.
- Design & media: Contrast Checker, Color Picker, Gradient Generator, Image Compressor, QR Code Maker, BMI Calculator (health utility), Unit Converter, Timezone Converter.

## Piping (text handoff)
Text-centric tools can pass content using sessionStorage so you avoid manual copy/paste:
- From Word Counter → Case Converter / Markdown Previewer / Text Diff (original or modified slot).
- From Case Converter → Word Counter / Markdown Previewer / Text Diff.
- From Markdown Previewer → Case Converter / Text Diff.
- Text Diff consumes the slot you choose (original vs modified).

## Offline & Updates
- Service worker at [sw.js](sw.js) pre-caches the app. Cache name bumps on updates (e.g., `microtools-v3`).
- Update banner appears when a new SW is ready; click **Update now** to activate and auto-reload.
- For stubborn caches, hard refresh (Ctrl/Cmd+Shift+R) or unregister the SW in DevTools → Application → Service Workers.

## Running Locally
1) Serve the folder (any static server). Examples:
   - Python: `python -m http.server 8000`
   - Node: `npx serve .`
2) Open http://localhost:8000/ and the service worker will cache assets after first load.

## Project Structure
- [index.html](index.html): landing grid linking all tools.
- [assets/styles.css](assets/styles.css): shared styling, gradients, cards, banners, meters.
- [assets/site.js](assets/site.js): service worker registration, toast helper, text handoff helpers.
- [tools/](tools/): individual tool pages (HTML + inline JS), all client-side.

## Notable UX Details
- Toasts live in the shared helper and are used for copy/clear actions.
- Strength/quality meters appear in Password Generator, Contrast Checker, BMI Calculator, etc.
- Copy buttons exist on most outputs; some tools support copy-to-clipboard of images (QR, Image Compressor).

## Content/SEO
- Each tool carries a unique title and meta description and 300+ words of body copy to satisfy content policies (e.g., AdSense requirements).
- Canonical flow is single-page-per-tool with no external deps for predictable performance.

## Privacy
- All computation is local; no analytics, no trackers, no network calls during tool usage.
- Clipboard operations request permission at use-time only.

## Maintenance
- When adding a tool: create `tools/<name>.html`, link it from [index.html](index.html), add to `ASSETS` in [sw.js](sw.js), and ensure at least ~300 words of explanatory copy.
- Bump the cache version in [sw.js](sw.js) when you add or rename files.
- Keep shared UX patterns (buttons, cards, meters) in `assets/styles.css` to avoid duplication.

## Keyboard Shortcuts
- Ctrl/Cmd+Enter: triggers primary action on most tools (e.g., generate, render, compare).
- Esc: clears memorable input on some tools; clears status in others depending on context.

## Contributing
- No build step; just static HTML/CSS/JS. Use any static server to preview.
- Lint manually for now (no configured linter). Keep scripts dependency-free and small.

Enjoy the speed and keep everything on-device.
