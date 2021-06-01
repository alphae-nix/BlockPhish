//script d'arriere plan
//Chrome analyse le fichier spécifié pour obtenir des instructions supplémentaires, telles que les événements importants qu'il doit écouter
let color = '#FFFFF'; //variable couleur

//ajout d'une routine d'ecoute
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  console.log('Default background color set to %cgreen', `color: ${color}`);
});

