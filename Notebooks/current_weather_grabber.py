#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os

def scrape_weather():
    
    # location of TrueWX 2 week weather forecast table
    url = "https://energy.truewx.com/degree-days/chart/gfs/conus/"
    
    # initializes selenium webdriver instance using Chromium 
    driver = webdriver.Chrome(executable_path=r'C:\Users\Nick\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    driver.implicitly_wait(10)

    # scrapes the relevant table
    current_weather_ = pd.read_html(driver.find_element_by_id("energy-table").get_attribute('outerHTML'))[0]
    
    # cleans table, dropping irrelevant data
    current_weather = pd.DataFrame(current_weather_)
    current_weather.columns = current_weather.columns.droplevel(0)
    current_weather_= current_weather.iloc[:, [7,8]]

    dropped = current_weather_.drop(current_weather_.index[[5,11,16,17,18]])
    save = dropped.reset_index(drop=True)
    
    save.index = pd.date_range(start='12/26/2020', periods=14, freq='D')
    
    # saves 14 day forecast data to csv
    file = save.to_csv('current_weather.csv')

    return file

