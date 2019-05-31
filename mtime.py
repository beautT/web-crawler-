# Selenium + Chrome 案例1
from selenium import webdriver
from selenium.webdriver.support.select import Select

global text
global project_name_list
global driver
import time
from rwCsv import *

UserInformation=["UserName","Information","birth","edu","edu2","job"]





#获取页面指定元素列表
def get_webtext(project_id):
    global driver
    global text

    text=[]
    text=driver.find_element_by_id(project_id).text
    #print(text)
    

#登录，获取首页文本
def open():
    global driver
    
    # 路径是自己解压安装 Chromedriver 的路径
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    

    url ="https://passport.mtime.com/member/signin/?redirectUrl=http%3A%2F%2Ftrade.mtime.com%2Fcart%2F"####################3
    xpath_name='//*[@id="loginEmailText"]'
    xpath_pwd='//*[@id="loginPasswordText"]'
    xpath_login='//*[@id="loginButton"]'


    driver.get(url)
    driver.find_element_by_xpath(xpath_name).clear()
    driver.find_element_by_xpath(xpath_name).send_keys("账号")
    driver.find_element_by_xpath(xpath_pwd).clear()
    driver.find_element_by_xpath(xpath_pwd).send_keys("密码")


    #定位“点击登录”框的位置的xpath，通过click()执行登录
    driver.find_element_by_xpath(xpath_login).click()

    
def close():
    global driver
    driver.quit()
    
     
url=readData("评论者id.csv")

if __name__=='__main__':

    
    #登录，获取首页文本
    open()
    for num in range(len(url)):
        html=url[num]
        time.sleep(1)
        global driver
        driver.get(html)
        try:
            name=driver.find_element_by_xpath('//*[@id="bodyRegion"]/div[1]/div[1]/div/div/div[2]/div/h3').text
        except:
            name="---"
        
        try:
            sex=driver.find_element_by_xpath('//*[@id="bodyRegion"]/div[1]/div[1]/div/div/div[2]/p[2]').text
        except:
            sex="---"
        
        
        try:
            birth= driver.find_element_by_xpath('//*[@id="bodyRegion"]/div[1]/div[3]/div/ul/li[1]').text
            
        except:
            birth="---"
            

        try:
            edu1 = driver.find_element_by_xpath('//*[@id="bodyRegion"]/div[1]/div[3]/div/p[4]').text
            
        except:
            edu1="-edu1-"
        
        try:
            
            edu2 = driver.find_element_by_xpath('//*[@id="bodyRegion"]/div[1]/div[3]/div/p[5]').text
            if edu2=="职业信息":
                edu2="---"
        except:
            edu2="--edu2-"
                
        try:
            job = driver.find_element_by_xpath('//*[@id="bodyRegion"]/div[1]/div[3]/div/p[8]').text
        except:
            job="---"
        UserInformation[0]=name
        UserInformation[1]=sex
        UserInformation[2]=birth
        UserInformation[3]=edu1
        UserInformation[4]=edu2
        UserInformation[5]=job
        writeData("用户信息.csv",UserInformation)
        print(UserInformation)


    close()



