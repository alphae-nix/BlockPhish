var precision;
let saveButton = document.getElementById("saveButton");
let precisionField = document.getElementById("precisionField");

chrome.storage.sync.get('StoredPrecision', function(data) {
  precision = data.StoredPrecision;
  precisionField.value = data.StoredPrecision;
  console.log(data.StoredPrecision);
})

saveButton.addEventListener("click", async() => {
  console.log("test1");
  chrome.storage.sync.set({ 'StoredPrecision': precisionField.value }, function() {
    console.log(precisionField.value);
  });
})
