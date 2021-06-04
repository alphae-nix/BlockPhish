//action lorsqu'on appuye sur le bouton dans .html
// Initialize button with user's preferred color
let startButton = document.getElementById("parser");


// When the button is clicked, inject setPageBackgroundColor into current page
startButton.addEventListener("click", async () => {
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
  var server = "http://127.0.0.1:5000/test";
  let xhr = new XMLHttpRequest();

  sender = JSON.stringify(arrayLinks)
  xhr.open('POST', server);
  xhr.setRequestHeader("Content-Type", "text/plain"); // application/json
  // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
  xhr.send(arrayLinks);
  xhr.onload = function() {
    var result = xhr.response.split(',');
    var length = result.length;
    result[0] = result[0].split('[')[1];
    result[length-1] = result[length-1].split(']')[0];
    
    alert(`Loaded: ${xhr.status} ${xhr.response}`);
  };

  console.log(arrayLinks);

};
