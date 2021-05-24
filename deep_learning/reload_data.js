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