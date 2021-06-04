import string
import numpy as np
import pandas as pd
import ipaddress
import whois
from datetime import datetime

#  1 seems legit
#  0 is suspicious
# -1 seems phishing

class urlToArray:
    
    def __init__(self, url):
        self.URLArray = self.URLtoARRAY(url)

    def contains_IP(self, url):
        ip = url.split('://')[1].split('/')[0]
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
        domain = url.split('://')[1].split('/')[0]
        if domain in str(short): return -1
        return 1

    def haveAt_URL(self, url):
        if '@' in url : return -1
        return 1

    def haveSlash_URL(self, url):
        if '//' in url.split('://')[1]: return -1
        return 1 

    def haveHyphen_URL(self, url):
        if '-' in url.split('://')[1].split('/')[0]: return -1
        return 1

    def haveSubDomain_URL(self, url):
        domain = url.split('://')[1].split('/')[0]
        if domain.startswith('www.') : domain = domain.split('www.')[1]
        if domain.count('.') == 1 : return 1
        if domain.count('.') == 2 : return 0
        return -1

    def haveHTTPS(self, url):
        if 'https' in url : return 1
        return -1

    def domainExpries_URL(self, url):
        domain = url.split('://')[1].split('/')[0]
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
        return array

    def getArray(self):
        return self.URLArray
