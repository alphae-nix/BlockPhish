import string
import numpy as np
import pandas as pd
import ipaddress
import whois
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse


#  1 seems legit
#  0 is suspicious
# -1 seems phishing

class urlToArray:
    
    def __init__(self, url):
        self.URLArray = self.URLtoARRAY(url)

    def contains_IP(self, url):
        ip = urlparse(url).netloc
        if ip.count('0x') >= 4 : return -1
        try:
            ipaddress.ip_address(ip)
            return -1
        except:
            return 1

    def length_URL(self, url):
        if len(url) > 75 : return -1 
        if len(url) >= 54 : return 0
        return 1

    def shortened_URL(self, url):
        short = ["bit.ly","cutt.ly","urlz","ow.ly","T.co","tinyurl","su.jinder","tiny.cc","bit.do","urls.fr"]
        domain = urlparse(url).netloc
        if domain in str(short): return -1
        return 1

    def haveAt_URL(self, url):
        if '@' in url : return -1
        return 1

    def haveSlash_URL(self, url):
        if '//' in url.split('://')[1]: return -1
        return 1 

    def haveHyphen_URL(self, url):
        if '-' in urlparse(url).netloc: return -1
        return 1

    def haveSubDomain_URL(self, url):
        domain = urlparse(url).netloc
        if domain.startswith('www.') : domain = domain.split('www.')[1]
        if domain.count('.') == 1 : return 1
        if domain.count('.') == 2 : return 0
        return -1

    def haveHTTPS(self, url):
        if 'https' in url.split('://')[0] : return 1
        return -1

    def domainExpries_URL(self, url):
        domain = urlparse(url).netloc
        try:
            info = whois.whois(domain)
            if info:
                expire = info.expiration_date[0] if type(info.expiration_date)==list else info.expiration_date
                now = datetime.now()
                ecart=(expire-now).days
                if ecart > 365 : return 1
                return -1
        except:
            return 0

    def favicon_URL(self, url):
        domain = urlparse(url).netloc
        try :
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page,"html.parser")
            icon_link = str(soup.find("link", rel="shortcut icon"))
            icon_link = icon_link.split('href="')[1].split('"')[0]
            icon_link = urlparse(icon_link).netloc
        except:
            return 0
        if domain == icon_link : return 1
        return -1

    def port_URL(self, url):
        standard_ports = [None,'80','443']
        strange_port = ['8443']
        port = urlparse(url).port
        if port in standard_ports : return 1
        if port in strange_port : return 0
        return -1
        
    def HTTPSdomain_URL(self, url):
        if 'https' in urlparse(url).netloc : return -1
        return 1

    def requestUrl_URL(self, url):
        try :
            domain = urlparse(url).netloc
            count = 0
            inside = 0

            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page,"html.parser")
            links = soup.find_all('a', href=True)

            for a in links :
                count += 1
                link = str(a['href'])
                if link.startswith('/') or domain == urlparse(link).netloc or '#' == link : inside += 1
            
            percent = (inside / count) * 100

            if percent > 61 : return 1
            if percent >= 22 : return 0
            return -1

        except:
            return 0    

    def anchor_URL(self, url):
        try :
            count = 0
            anchor = 0

            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page,"html.parser")
            links = soup.find_all('a', href=True)

            for a in links :
                count += 1
                link = str(a['href'])
                if link.startswith('#') or link == "JavaScript ::void(0)" : anchor += 1
            
            percent = (anchor / count) * 100

            if percent > 67 : return -1
            if percent >= 31 : return 0
            return 1

        except:
            return 0 

    def links_meta_URL(self, url):
        try :
            count = 0
            links = 0
            domain = urlparse(url).netloc
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page,"html.parser")

            for tag in soup.find_all("meta",property=True):
                if tag.get("property") == "og:url":
                    count += 1
                    if urlparse(tag.get("content",None)).netloc == domain:
                        links += 1

            for tag in soup.find_all("script",src=True):
                count+=1
                if urlparse(tag.get("src",None)).netloc == domain:
                    links += 1

            for tag3 in soup.find_all("link",href=True):
                count += 1
                if urlparse(tag3.get("href")).netloc == domain:
                    links += 1

            percent = (links / count) * 100

            if percent > 81 : return 1
            if percent >= 17 : return 0
            return -1   
        except :
            return 0

    def URLtoARRAY(self, url):
        array = []
        array.append(self.contains_IP(url))
        array.append(self.length_URL(url))
        array.append(self.shortened_URL(url))
        array.append(self.haveAt_URL(url))
        array.append(self.haveSlash_URL(url))
        array.append(self.haveHyphen_URL(url))
        array.append(self.haveSubDomain_URL(url))
        array.append(self.haveHTTPS(url))
        array.append(self.domainExpries_URL(url))
        array.append(self.favicon_URL(url))
        array.append(self.port_URL(url))
        array.append(self.HTTPSdomain_URL(url))
        array.append(self.requestUrl_URL(url))
        array.append(self.anchor_URL(url))
        array.append(self.links_meta_URL(url))
        return array


    def getArray(self):
        return self.URLArray
