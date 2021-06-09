//script d'arriere plan
//Chrome analyse le fichier spécifié pour obtenir des instructions supplémentaires, telles que les événements importants qu'il doit écouter

chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ 'StoredPrecision': 80 }, function() {
  });
});
