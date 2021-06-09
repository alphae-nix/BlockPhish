//script d'arriere plan
//Chrome analyse le fichier spécifié pour obtenir des instructions supplémentaires, telles que les événements importants qu'il doit écouter

//ajout d'une routine d'ecoute
chrome.runtime.onInstalled.addEventListener(() => {
  chrome.storage.sync.set({ 'StoredPrecision': 80 }, function() {
  console.log("ok");
  });
});
