self.addEventListener('install', function(event) {
  // Perform install steps (can cache files here)
  self.skipWaiting();
});

self.addEventListener('activate', function(event) {
  // Activate event
  return self.clients.claim();
});

self.addEventListener('fetch', function(event) {
  // Optionally handle fetch events for offline support
}); 