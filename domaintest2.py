# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:06:00 2018

@author: ksingh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:05:19 2018

@author: ksingh
"""

from selenium import webdriver
from time import sleep
import random as rn
import re
import pymongo
from pymongo import MongoClient
import json 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import psycopg2
import time
import pymysql
import os
from selenium.webdriver.chrome.webdriver import WebDriver
import os
import itertools
from selenium.common.exceptions import NoSuchElementException

'''def merge_two_dicts(x, y):
    z = x.copy()   
    z.update(y) 
    return z
    insert_mongodb(z)'''
    

def create_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    #options.add_argument("headless")
    executable_path= "C:\\Users\\ksingh\\Desktop\\codes\\driver\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path= executable_path, chrome_options=options)
    driver.maximize_window()
    sleep(2)
    driver.get("https://google.com")
    sleep(3)
    
    try:
        driver.get(url)
        sleep(2)
        sign=driver.find_element_by_xpath ('//*[@id="join-form"]/p[3]/a')
        sign.click()
        username = driver.find_element_by_id("login-email")
        username.send_keys("keshavjain16@outlook.com")
        password = driver.find_element_by_id("login-password")
        password.send_keys("P@7020627474")
        sndbutton = driver.find_element_by_id("login-submit")
        sndbutton.submit()
        sleep(2)
   
        moreinfo=driver.find_element_by_id("org-about-company-module__show-details-btn")
        sleep(2)
        moreinfo.click()
    except NoSuchElementException as exception:
         #print ("Element not found and test failed")
         return 1
   
    
    sleep(2)
    extracted_aboutus={}
    clean_data={}
    
    #fetched_data=driver.find_element_by_id("ember1853").text
    try:
        sleep(1)
        data_about=driver.find_element_by_class_name("org-about-company-module__about-us-left-column").text
        #print(data_about)
        data1= {"about_us":data_about}     
        extracted_aboutus.update(data1)
    except NoSuchElementException as exception:
       # data_about=driver.find_element_by_class_name("org-about-us-organization-description ember-view").text
        #print(data_about)
        sleep(2)
        return 1
   
    #print(extracted_aboutus)
   
    try:
        sleep(1)
        fetched_data=driver.find_element_by_class_name(" org-about-company-module__about-us-extra-left-column").text
        #print(fetched_data)
    except NoSuchElementException as exception:
        fetched_data=driver.find_element_by_class_name("org-about-company-module__about-us-extra").text
        #print(fetched_data)
        sleep(2)  
        pass
        
   
    # print(fetched_data)
    
    sleep(2)
    fetched_data_dict=dict(itertools.zip_longest(*[iter(fetched_data.split('\n')[1:12])]*2,fillvalue=""))
    #print(fetched_data_dict)
    clean_data.update(fetched_data_dict)
   
    z = dict(itertools.chain(extracted_aboutus.items(),clean_data.items()))
    print(z)
    #insert_mongodb(z)
    return driver
    driver.close
    
    
      

def insert_mongodb(dic):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['domain']
    collection = db['domain_data']
    collection.insert_one(dic) 
    print('inserted into mongo' )  


    

company_name=input("Please enter company name :")
link=f"https://www.linkedin.com/company/{company_name}"
create_driver(link)
  
