import requests
import re
from bs4 import BeautifulSoup
import sys
import datetime

def movName(movId):
    url = "http://movie.mtime.com/"+str(movId)+"/"

   

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; \Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    soup= BeautifulSoup(r.text,"lxml")
    return soup.find('div',class_="db_head").h1.string
    



