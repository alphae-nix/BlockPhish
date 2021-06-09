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



function parser() {
  var precision = 0;
  //loader la valeur stockée pour faire la comparaison
  chrome.storage.sync.get('StoredPrecision', function(data) {
    precision = data.StoredPrecision;
    console.log(precision)
  })

  var links = document.links;
  var arrayLinks = [];
  for (let i=0; i < links.length; i++){
    link = String(links[i]);
    var lastC = link.charAt(link.length-1);
    if(lastC == '/'){
      link = link.slice(0, -1);
    }
    arrayLinks.push(link);
  }
  var server = "http://127.0.0.1:5000/test";
  let xhr = new XMLHttpRequest();

  sender = JSON.stringify(arrayLinks)
  xhr.open('POST', server);
  xhr.setRequestHeader("Content-Type", "text/plain"); // application/json
  // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
  xhr.send(arrayLinks);
  xhr.onload = function() {
    var result = xhr.response.split(', ');
    var length = result.length;
    result[0] = result[0].split('[')[1];
    result[length-1] = result[length-1].split(']')[0];
    console.log(result);
    console.log(arrayLinks);

    for(let i=0; i<result.length; i++){
      var allElements = document.getElementsByTagName('*');
      var link = "";
      console.log(arrayLinks[i]);
      for (var j = 0, n = allElements.length; j < n; j++) {
        console.log(allElements[j].getAttribute("href"));
        if (allElements[j].getAttribute("href") == arrayLinks[i]) {
          link = allElements[j];
        }
      }
      console.log(result[i]);
      if(parseFloat(result[i]) < parseFloat(precision)){
        try {
          link.style.color = 'red';
        } catch (error){};
      }
    };
  }
}
