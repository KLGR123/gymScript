from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
import re

driver = webdriver.Chrome("chromedriver.exe") 
driver.get(r'https://gym.byr.moe/login.php')
driver.find_element_by_xpath('//*[@id="username"]').send_keys("2019210514") #学号
driver.find_element_by_xpath('//*[@id="password"]').send_keys("aty26137") #密码
driver.find_element_by_xpath('//*[@id="submit-button"]').click()

driver.find_element_by_xpath('//*[@id="bookList"]/ul/li[1]/div[1]').click()

a = '//*[@id="20210329"]/div[1]'
sig = driver.find_element_by_xpath(a + '/div[3]').text
print('div1:' + sig)


a = '//*[@id="20210329"]/div[2]'
sig = driver.find_element_by_xpath(a + '/div[3]').text
print('div2:' + sig)


a = '//*[@id="20210329"]/div[3]'
sig = driver.find_element_by_xpath(a + '/div[3]').text
print('div3:' + sig)

#//*[@id="20210329"]/div[1]/div[3]
#//*[@id="20210329"]/div[2]/div[3]
#//*[@id="20210329"]/div[3]/div[3]