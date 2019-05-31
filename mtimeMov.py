import requests
import re
from bs4 import BeautifulSoup
import csv
import sys
import datetime
import sys
from rwCsv import *
from mtimeP import *
from mtimeC import *
#处理 UNicodeENCODEERROR
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

movText = ["MovName",
           "MovTime",
           "MovData",
           "MovType",
           "PnameMod",
           "MovEoi",
           "MovDoi",
           "MovMcompany",
           "MovPcompany"]
         


def openWeb(movId):
    url = "http://movie.mtime.com/"+str(movId)+"/"
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; \Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}
    r = requests.get(url,  headers=headers)
    r.encoding = 'utf-8'
    #print("网页请求状态码：%s\n"%r.status_code)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"lxml")
    else:
        return r.status_code




def getMovName(movId):
    soup = openWeb(movId)
    try:    
        return soup.find('div',class_="db_head").h1.string
    except:
        return None

def getMovType(soup):
    #soup=openWeb(movId)
    try:
        #print(getMovType(soup).find_all("a")[2])
         #movt=getMovType(soup).split("-")
         #print(movt[0])
        return soup.find('div',class_="otherbox __r_c_").get_text()
    except:
        return None


def saveMovType(movId,num):
    soup=openWeb(movId)
    movt=getMovType(soup).split("-")
    act=movt[num]
    return act


print(saveMovType(10190,1))

movId=readData("时光.csv")
def run():
    for i in range(1,21):
        movText[0]=getMovName(movId[i])
        movText[1]=saveMovType(movId[i],0)
        movText[2]=saveMovType(movId[i],2)
        movText[3]=saveMovType(movId[i],1)
        movText[4]=savePnameMod(movId[i])
        movText[5]=getMovEoi(movId[i])
        movText[6]=getMovDoi(movId[i])
        movText[7]=getMovMcompany(movId[i])
        movText[8]=getMovPcompany(movId[i])
        print(movText)
        
run()
        
    




