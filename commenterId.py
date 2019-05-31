import requests
import re
from bs4 import BeautifulSoup
import csv
import sys
import datetime
import sys
from rwCsv import *
from MovieName import *
#处理 UNicodeENCODEERROR
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

movText = ["UserName",
           "UserScore",
           "UserCtime",
           "MovComment"]
         

def getUserLink(soup):
    try:  
        #return soup.find_all('div',class_="pic_58")[num].a["href"]
        return soup.find_all('div',class_="pic_58")
    except :
        return None

def write_csv(data_row):
    path  = "评论者id.csv"
    with open(path,'a+',encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)



def openIndexWeb(movId):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    for i in range(10):
        if i == 0:
            url = "http://movie.mtime.com/"+str(movId)+"/reviews/short/new.html"
        else:
            url= "http://movie.mtime.com/"+str(movId)+"/reviews/short/new-{}.html".format(str(i+1))
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        #print("网页请求状态码：%s\n"%r.status_code)
        soup = BeautifulSoup(r.text,"lxml")
        print(len(getUserLink(soup)))
        
       
        for num in range(len(getUserLink(soup))):
            act=[]
            act.append(getUserLink(soup)[num].a["href"])
            write_csv(act)
           
                
  




movId=readData("时光.csv")
def run():
    for i in range(100):
        soup = openIndexWeb(movId[i])
        
    
run()



