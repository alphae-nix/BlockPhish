// Copyright (C) 2021  DELATTE_JAILLLON_HERMANN_PERESSE-GOURBIL
// 
// This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or  any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License along with this program; if not, go on http://www.gnu.org/licenses/gpl-3.0.html or write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


// import * as tf from '@tensorflow/tfjs';

// const model = tf.loadLayersModel('https://perso.esiee.fr/~delattel/projetE3/model.yaml');
// console.log(model.summary)

var jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;

var $ = jQuery = require('jquery')(window);


// function postData(input) {
//     $.ajax({
//         type: "POST",
//         url: "/home/alphae/projetE3/projetE3/test.py",
//         data: { param: input },
//         success: callbackFunc
//     });
// }

// function callbackFunc(response) {
//     // do something with the response
//     console.log(response);
// }

// postData('https://facebook.com');

function runPyScript(input){
    var jqXHR = $.ajax({
        type: "POST",
        url: "/home/alphae/projetE3/projetE3/test.py",
        async: false,
        data: { param: input }
    });

    return jqXHR.responseText;
}

// do something with the response
response= runPyScript('https://facebook.com');
console.log(response);
