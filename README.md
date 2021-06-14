# E3 project : Block Phish


## How it work ?
### Start the analyse
Open you web extension and click on the "start" button. Wait few minutes for the analyse result. 

### Analyse
The web extension collect all links on the current page. It send them to a python server. All links are passed in 15 functions which look at characteristics like : length of url, using shorting services (bit.li), using weard symbol @ // #, multi sub domains, ...

Then, it return a array of [1, 0, -1] for each link. And each array is analysed by a neural network (deep learning). It return a percent that corresponds to a phishing prediction. 

### Result
This result for each link is send to the web extension. It change malicious link in red color on the page and a alert message appear on the web extension. For more security, malicious link are unavailable. You can go on thanks a confirm window. 


## More about the extension
### Parameters
User can change your level of risk acceptation. For example if our AI is sure at 85% that this is a phishing link would you like to identify it as phishing or not. Here we can specify from 50 to 100 %.

### Name inspiration
*Block Phish* is a reference to stopping phishing links. 

*Phish* is an abreviation of phishing, but it can make you think about fish (look at our icon : it is a hook !). 
*Block Phish* also can make you think about *AdBlock* an extension to stop publicity popup. 



## Launch
git clone
pip -r requierement.txt
