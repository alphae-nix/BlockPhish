//action lorsqu'on appuye sur le bouton dans .html
// Initialize button with user's preferred color
let changeColor = document.getElementById("parser");

chrome.storage.sync.get("color", ({ color }) => {
  changeColor.style.backgroundColor = color;
});

// When the button is clicked, inject setPageBackgroundColor into current page
changeColor.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: parser,
  });
});

// The body of this function will be executed as a content script inside the
// current page
function parser() {
  var links = document.links;
  var arrayLinks = [];
  for (let i=0; i < links.length; i++){
    arrayLinks.push(links[i].href);
  }
  console.log(arrayLinks);

}
