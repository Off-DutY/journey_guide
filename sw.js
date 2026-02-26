const CACHE_NAME = 'europe-trip-v1';

// 需要快取的核心資源
const CORE_ASSETS = [
    './',
    './index.html',
    './plan.json',
    'https://cdn.tailwindcss.com',
    'https://unpkg.com/lucide@latest'
];

// 安裝階段：快取所有核心資源
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(CORE_ASSETS))
            .then(() => self.skipWaiting())
    );
});

// 啟動階段：清除舊版快取
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys =>
            Promise.all(
                keys.filter(key => key !== CACHE_NAME)
                    .map(key => caches.delete(key))
            )
        ).then(() => self.clients.claim())
    );
});

// 攔截請求：Network First（優先網路，失敗時用快取）
self.addEventListener('fetch', event => {
    event.respondWith(
        fetch(event.request)
            .then(response => {
                // 網路成功：更新快取後回傳
                const clone = response.clone();
                caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
                return response;
            })
            .catch(() => {
                // 網路失敗：從快取回傳
                return caches.match(event.request);
            })
    );
});
