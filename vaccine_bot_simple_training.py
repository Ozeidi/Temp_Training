'''
    ***************************************************
    ***************************************************
    Script: Vaccine Status Bot
    Author: OZeidi, ozeidi91@gmail.com
    Description: Fetch Vacine Status from MOH COVID19 Website
    Version: V1.0
    Last Modification: 17th Sep 2021
    ***************************************************
    ***************************************************

*/

// Required Packages
'''

from pandas.core.dtypes.missing import isna
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
####
# Needed for the wait_for_xpath fucntion
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


import os
# from urllib.request import urlopen
import pandas as pd
import numpy as np
# import requests
# import csv
# import datetime
import time
import random
import pickle
# Change this to the path of your chrome Driver
dirpath = "/home/ozeidi/00.coding/Linkedin-Job-Scraper/chromedriver"


def wait_for_xpath( broswer, xpath):
    wait = WebDriverWait(broswer, 10)
    ui = wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
    ActionChains(broswer).move_to_element(ui).perform()
    return ui


def browser_options():
    options = Options()
    #options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("user-agent=Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393")
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    #options.add_argument('--disable-gpu')
    #options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    return options

def start_browsing():
    res = {}
    
    browser = webdriver.Chrome(chrome_options=browser_options(), executable_path = dirpath )
    print("Loading the page\n ")
    browser.get("https://covid19.moh.gov.om/#/check-certificate")
    df = pd.read_excel('data/PDO Staff with ID No. 19 09 2021.xlsx')
    



def check_status(browser, ID):
    try:
        #browser.get("https://covid19.moh.gov.om/#/check-certificate")
        
        civil_id_txtbox =  wait_for_xpath(browser,'//*[@id="mat-input-1"]')#browser.find_element_by_xpath('//*[@id="mat-input-1"]')
        civil_id_txtbox.send_keys(ID)
        # Click the button to check the status
        #time.sleep(2)
        btn = wait_for_xpath(browser, '//*[@id="loader"]/main/vacccert/div/div[3]/div/button')
        btn.click()
        try:
            vac_table = wait_for_xpath(browser,'//*[@id="loader"]/main/vacccert/div/div[4]/div[2]/table')
            # vac_table = browser.find_element_by_xpath('//*[@id="loader"]/main/vacccert/div/div[4]/div[2]/table')
            vac_status = vac_table.text 
            # btn = wait_for_xpath(browser,'//*[@id="loader"]/main/vacccert/div/div[4]/div[3]/button')
            # btn.click()
            browser.execute_script("document.querySelector('#loader > main > vacccert > div > div.wizard-panel.ng-star-inserted > div.text-center > button').click()")
            
        except :
            vac_status = "NOT VACCINATED"
            browser.execute_script("document.querySelector('#loader > main > vacccert > div > div.wizard-panel.ng-star-inserted > div:nth-child(2) > button').click()")

        #browser.get("https://covid19.moh.gov.om/#/check-certificate")
        # time.sleep(1)
        #browser.execute_script("document.querySelector('#loader > main > vacccert > div > div.wizard-panel.ng-star-inserted > div.text-center > button').click()")

        # # WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="loader"]/main/vacccert/div/div[4]/div[3]/button'))).click()
        # print('Return Back Clicked')
        return vac_status
    except TimeoutException:
        print("Error")
        browser.get("https://covid19.moh.gov.om/#/check-certificate")





start_browsing()

