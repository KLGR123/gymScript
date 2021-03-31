############
#firstly base on your own Chrome, download chromedriver.exe
#then put it in this file
############

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import re

stime = 1
rtime = 1

############
#def download_website():
#    url = 'https://gym.byr.moe/index.php'
#    html = urllib.request.urlopen(url).read()
#    
#    with open('htmlContent.txt', 'wb') as f:
#        f.write(html) 
#        print('download successfully!')
#        f.close()
############

def get_date():
    date = time.strftime("%Y%m%d")
    print(date)
    return date

def get_tomo():
    temp_date = datetime.datetime.now()
    tomo = (temp_date + datetime.timedelta(days=+1)).strftime("%Y%m%d")
    return tomo

def get_tomo2():
    temp_date = datetime.datetime.now()
    tomo2 = (temp_date + datetime.timedelta(days=+2)).strftime("%Y%m%d")
    return tomo2

def get_tomo3():
    temp_date = datetime.datetime.now()
    tomo3 = (temp_date + datetime.timedelta(days=+3)).strftime("%Y%m%d")
    return tomo3

def judge_available(date, path, driver): 
    driver.find_element_by_xpath(path).click()  
    print('on running:' + str(date))
    time.sleep(rtime)

    for i in range(1, 4):
        driver.find_element_by_xpath(path).click() 
        a = '//*[@id="{}"]/div[{}]'.format(date, i)
        sig = driver.find_element_by_xpath(a + '/div[3]').text
        print('original sig:' + sig)
        sig = sig[0:2]

        if sig == '40': 
            print('full now or already booked!')
            driver.find_element_by_xpath(a).click()
            time.sleep(rtime)
            driver.find_element_by_xpath('//*[@id="submit"]').click()
            time.sleep(rtime)
            driver.find_element_by_xpath('//*[@id="back"]').click()

        else:
            print('now sig:' + str(sig))
            print('avaiable!')
            #if driver.find_element_by_xpath(a).is_enabled():
            driver.find_element_by_xpath(a).click()
            print('节点1')
            time.sleep(rtime)
            driver.find_element_by_xpath('//*[@id="submit"]').click()
            time.sleep(rtime)

            print('successfully booked!')
            driver.find_element_by_xpath('//*[@id="back"]').click()

        time.sleep(0.7)  

def run():
    driver = webdriver.Chrome("chromedriver.exe") 
    driver.get(r'https://gym.byr.moe/login.php')
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("2019210517") #学号
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("04294511") #密码
    driver.find_element_by_xpath('//*[@id="submit-button"]').click()

    today = get_date()
    tomo = get_tomo()
    tomo2 = get_tomo2()
    tomo3 = get_tomo3()

    while True:
        ntime = int(time.strftime("%H"))
        print('present time hour:' + str(ntime))

        if ntime >= 22 or ntime < 17:
            if ntime >= 22 and ntime < 24:
                judge_available(tomo, '//*[@id="bookList"]/ul/li[1]/div[1]', driver)
                time.sleep(stime)
                judge_available(tomo2, '//*[@id="bookList"]/ul/li[2]/div[1]', driver)
                time.sleep(stime)
                judge_available(tomo3, '//*[@id="bookList"]/ul/li[3]/div[1]', driver)
                time.sleep(stime)
            else:
                judge_available(today, '//*[@id="bookList"]/ul/li[1]/div[1]', driver)
                time.sleep(stime)
                judge_available(tomo, '//*[@id="bookList"]/ul/li[2]/div[1]', driver)
                time.sleep(stime)
                judge_available(tomo2, '//*[@id="bookList"]/ul/li[3]/div[1]', driver)
                time.sleep(stime)
        else:
            judge_available(tomo, '//*[@id="bookList"]/ul/li[1]/div[1]', driver)
            judge_available(tomo2, '//*[@id="bookList"]/ul/li[2]/div[1]', driver)

        driver.refresh()
        time.sleep(rtime)

    driver.quit()

if __name__ == "__main__":
    run()
    
    