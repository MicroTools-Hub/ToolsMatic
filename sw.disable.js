const CACHE_NAME = 'microtools-v3';
const ASSETS = [
  '/',
  '/index.html',
  '/assets/styles.css',
  '/assets/site.js',
  '/tools/word-counter.html',
  '/tools/password-generator.html',
  '/tools/quote-generator.html',
  '/tools/case-converter.html',
  '/tools/gradient-generator.html',
  '/tools/json-formatter.html',
  '/tools/base64-encoder.html',
  '/tools/image-compressor.html',
  '/tools/qr-code-maker.html',
  '/tools/contrast-checker.html',
  '/tools/jwt-inspector.html',
  '/tools/csv-inspector.html',
  '/tools/bmi-calculator.html',
  '/tools/markdown-previewer.html',
  '/tools/regex-tester.html',
  '/tools/uuid-maker.html',
  '/tools/url-encoder.html',
  '/tools/color-picker.html',
  '/tools/unit-converter.html',
  '/tools/timezone-converter.html',
  '/tools/text-diff-checker.html',
  '/tools/lorem-ipsum-generator.html',
  '/tools/csv-to-json.html',
  '/tools/html-minifier.html',
  '/tools/number-converter.html'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('message', (event) => {
  if (event.data === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET') return;
  event.respondWith(
    caches.match(request).then((cached) => {
      if (cached) return cached;
      return fetch(request).then((resp) => {
        const clone = resp.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
        return resp;
      }).catch(() => cached);
    })
  );
});
