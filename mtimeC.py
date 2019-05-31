import requests
import re
from bs4 import BeautifulSoup
import csv
import sys
import datetime
import sys

#处理 UNicodeENCODEERROR
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def opencreditsWeb(movId):
    url = "http://movie.mtime.com/"+str(movId)+"/details.html#company"



    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; \Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    r = requests.get(url,  headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"xml")
    else:
        return r.status_code



def getMovMcompany(movId):
    soup=opencreditsWeb(movId)
    try:
        
        return soup.find('div',class_="fl wp49").text
    except:
        return None


def getMovPcompany(movId):
    soup=opencreditsWeb(movId)
    try:
        
        return soup.find('div',class_="fl wp49").find_next('div').text
    except:
        return None




