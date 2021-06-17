// Copyright (C) 2021  DELATTE_JAILLLON_HERMANN_PERESSE-GOURBIL
// 
// This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or  any later version.
// 
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License along with this program; if not, go on http://www.gnu.org/licenses/gpl-3.0.html or write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


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
