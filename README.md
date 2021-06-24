

# ESIEE Paris Student project : Block Phish

## Project description

This project has been made for "Day of project 2021" for [ESIEE Paris](https://www.esiee.fr/). This project is composed in 2 parts : 

- The first part is a web extension for chrome web browser. This extension analyse your web page, and alarm you if a phishing link is detected
- The second part is the server. It is the back part of this project. It analyses your mail, and make a prediction about your link

----------------------------------

## How it works ?

### Start the analysis

Open your web extension and click on the "start" button. Wait few minutes for the analysis result. 

### Analyse

The web extension collect all links on the current page. It sends them to a python server. All links are passed in 15 functions which look at characteristics like : length of URL, using shorting services (bit.li), using weird symbol @ // #, multi subdomains, ...

Then, it returns an array of [1, 0, -1] for each link. And each array is analysed by a neural network (deep learning). It returns a percent that corresponds to a phishing prediction. 

### Result

This result for each link is sent to the web extension. It changes malicious link in red color on the page and an alert message appear on the web extension. For more security, malicious link are unavailable. You can go on, thanks a confirm window. 

-----------------

## More about the extension

### Parameters

User can change your level of risk acceptation. For example if our AI is sure at 85% that this is a phishing link would you like to identify it as phishing or not. Here we can specify from 50 to 100 %.

### Name inspiration

*Block Phish* is a reference to stopping phishing links. 

*Phish* is an abbreviation of phishing, but it can make you think about fish (look at our icon : it is a hook !). 
*Block Phish* also can make you think about *AdBlock* an extension to stop publicity pop-up. 

----------------------------------

## Launch

### Install the extension

1. Download the [project](https://github.com/alphae-nix/projetE3/archive/refs/heads/main.zip)
2. Go to [the Chrome extension page](chrome://extensions)
3. Enable *developer mode*
4. Click *Load unpacked extension*
5. Choose the *extension* folder and load
6. Enjoy

### Install the server

1. Download the [project](https://github.com/alphae-nix/projetE3/archive/refs/heads/main.zip)
2. Install requirements

  ```python
  pip -r requierment.txt
  ```

  You could face some problems with TensorFlow depending on your graphic card

3. Set Flask path 

  - For Windows : 

  ```bash
  cd back
  set FLASK_APP = app.py
  ```

  - For Linux :

  ```bash
  cd back
  export FLASK_APP = app.py
  ```

4. Run Flask server

  ```bash
  flask run
  ```

  Or :

  ```bash
  python -m flask run
  ```

----

## Demo

Careful, don't click on bad links ! It’s just for test the extension

- [Facebook.com  - safe link #1](https://www.facebook.com/) ✅
- [Google.fr - safe link #2](https://www.google.fr/) ✅
- [Linkedin.com - safe link #3](https://www.linkedin.com/) ✅
- [bad link #1](https://dsewrdeeds5.s3.eu-gb.cloud-object-storage.appdomain.cloud/homoeochromatic/index.html#eimaste@stinpriza.org) ❌
- [bad link #2](https://pay116-olx.info) ❌
- [bad link #3](https://ipkobiznes.cc/auth/login/) ❌

----------------------------------

## Contact

If you have any questions or comments about this project, or need help using it, please either raise an issue or contact us.

- [Thomas Jaillon](mailto:thomas.jaillon@edu.esiee.fr) *github:* alias [@jaillont](https://github.com/jaillont)
- [Manon Hermann](mailto:manon.hermann@edu.esiee.fr) *github:* alias [@CappiLucky](https://github.com/CappiLucky)
- [Laurent Delatte](mailto:laurent.delatte@edu.esiee.fr) *github:* alias [@alphae-nix](https://github.com/alphae-nix)
- [Theo Peresse-Gourbil](mailto:theo.peresse-gourbil@edu.esiee.fr) *github:* alias [@blackjack-nix](https://github.com/blackjack-nix)

