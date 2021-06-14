//popup start button
let startButton = document.getElementById("parser");

//hidden elements revelated when needed
var danger = document.getElementById("danger");
var safe = document.getElementById("safe");
var analyse = document.getElementById("analysisResults");
var loader = document.getElementById("loader");


// When the button is clicked, inject parser into current page
startButton.addEventListener("click", async () => {
  //when click, show analyse and loader
  
  //hide results from previous analyse
  safe.style.display = "none";
  danger.style.display = "none";

  //get all tabs from chrome
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  //launch script in the page
  await chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: parser,
  },)
})



async function parser() {

  chrome.runtime.sendMessage("PhishDetector "+ "load");

  // ## partie précision
  var precision = 0; 
  chrome.storage.sync.get('StoredPrecision', function(data) {
    precision = data.StoredPrecision;
    if (parseFloat(precision) == parseFloat(100)){
      precision = parseFloat(0.999)
    }
  })//load la précision depuis le storage chrome

  // ## partie traitement des liens
  var links = document.links;
  var arrayLinks = [];
  for (let i=0; i < links.length; i++){
    link = String(links[i]);
    var lastC = link.charAt(link.length-1);
    if(lastC == '/'){
      link = link.slice(0, -1);
    }
    if (link.substring(0,4) !== "http") {
      continue;
    }
    arrayLinks.push(link);
  }

  // ## Partie requete
  var server = "https://127.0.0.1:5000/test";
  let xhr = new XMLHttpRequest();

  sender = JSON.stringify(arrayLinks)
  xhr.open('POST', server);
  xhr.setRequestHeader("Content-Type", "text/plain"); // application/json
  // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
  xhr.send(arrayLinks);
  xhr.onload = function() {
    // ## partie traietement de la réponse
    var result = xhr.response.split(', ');
    var length = result.length;
    var safeBool = true;

    //nettoyage de la réponse
    result[0] = result[0].split('[')[1];
    result[length-1] = result[length-1].split(']')[0];

    //on cherche le lien qui a le bon href href 
    for(let i=0; i<result.length; i++){
      (function () {
        var allElements = document.getElementsByTagName('*');
        var link;
        for (var j = 0, n = allElements.length; j < n; j++) {
          if (allElements[j].getAttribute("href") == arrayLinks[i] || allElements[j].getAttribute("href") == String(arrayLinks[i] + '/')) {
            link = allElements[j];
            break;
          }
        }
    
        // on compare la réponse a la précision
        if(parseFloat(result[i]) < parseFloat(precision)){
          console.log(result[i]);
          safeBool = false;
          link.setAttribute("style","color:red;");

          link.addEventListener("click", function(){
            let href = link.getAttribute("href");
            link.setAttribute("href","javascript:;");
            let confirmation = confirm("This link has been identified has malicious. Do you really want to go ?");
            if(confirmation === true){
              link.setAttribute("href",href);
              window.location.href = href;
            }
          })
    
        }
      }()); 
    };
  //on envoi un message a la popup avec le résultat de l'analyse
  chrome.runtime.sendMessage("PhishDetector "+ safeBool);
}
}

//on capte le message
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  sign = message.split(' ')[0];
  value = message.split(' ')[1];
  if(sign == "PhishDetector"){
    loader.style.display = "none";
    if (value == "false") {
      danger.style.display = "block";
    } else if ( value == "true"){
      safe.style.display = "block";
    } else if (value == "load") {
      analyse.style.display = "block";
      loader.style.display = "block";
    }
  }
  
});
