var slider = document.getElementById("myRange");
var output = document.getElementById("value");

output.innerHTML = slider.value;
slider.oninput = function(){
    output.innerHTML = this.value;
}

slider.addEventListener("mouseMove",function(){
    var x = slider.value;
    var color = 'linear-gradient(90deg,rgb(117,252,117)'+x+'%,rgb(214,214,214)'+x+'%);';
    slider.style.background = color;
})

slider.addEventListener("mouseleave", function(){
    var x = slider.value;
    chrome.storage.sync.set({ 'StoredPrecision': x }, function() {
        console.log(x);
    });
})

window.addEventListener("load", function(){
    chrome.storage.sync.get('StoredPrecision', function(data) {
        slider.value = data.StoredPrecision;
        var x = slider.value;
        var color = 'linear-gradient(90deg,rgb(117,252,117)'+x+'%,rgb(214,214,214)'+x+'%);';
        slider.style.background = color;
        output.innerHTML = x;
      });
})
