#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randrange
from tqdm import tqdm
from config import Username,Password
import time
import os
import re
import shutil
import glob
import sys


# In[2]:


def Driver_Properties(download_folder):
    options = Options()
    options = wb.ChromeOptions()
    prefs = {
            "download.default_directory": download_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.disable_download_protection": True,
            "safebrowsing.enabled": True
            }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("window-size=1200x600")
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    driver = wb.Chrome(options=options)
    return driver


# In[3]:


def Linkedin_Login(Username,Password):
    driver.get('https://www.linkedin.com/login')
    username = driver.find_element_by_id('username')
    username.send_keys(Username)
    passwd = driver.find_element_by_id('password')
    passwd.send_keys(Password)
    passwd.send_keys(Keys.ENTER)
    time.sleep(2)


# In[4]:


def Search_Role(role):
    s = driver.find_element_by_class_name('nav-search-typeahead')
    sr = s.find_element_by_class_name('search-global-typeahead__input')
    sr.send_keys(role)
    sr.send_keys(Keys.ENTER)
    time.sleep(2)
    #navigate to People tab
    ao = driver.find_element_by_class_name('authentication-outlet')
    ng = ao.find_element_by_class_name('neptune-grid')
    sf = ng.find_element_by_class_name('search-filters-bar') 
    people = sf.find_element_by_class_name('search-vertical-filter__filter-item').click()
    time.sleep(2)


# In[5]:


def Filter_Location(location):
    l = driver.find_element_by_class_name('peek-carousel')
    l.find_element_by_class_name('search-s-facet--geoRegion').click()
    to = driver.find_element_by_xpath("//input[@role='combobox'][@placeholder='Add a country/region']") # changed from l to driver
    to.clear
    to.send_keys(location)
    time.sleep(2)
    to.send_keys(Keys.DOWN, Keys.RETURN)
    driver.find_elements_by_tag_name('button')[11].click()


# In[6]:


def Get_Page_Urls(page_limit):
    page_urls = []
    initial_url = driver.current_url
    page_urls.append(initial_url)
    for i in range(2,page_limit):
        url = initial_url+"&page=" + str(i)
        page_urls.append(url)
    return page_urls 


# In[7]:


def Profile_Links(page_urls):
    profilelinks = []
    for i in tqdm(page_urls):
        driver.get(i)
        results = driver.find_elements_by_class_name("search-result__occluded-item")
        for result in results:
            hover = ActionChains(driver).move_to_element(result)
            hover.perform()
            time.sleep(randrange(3,6))
            links = result.find_element_by_class_name('search-result__result-link').get_property('href')
            profilelinks.append(links)
            time.sleep(randrange(3,6))
    return profilelinks


# In[8]:


def download_wait(directory, timeout, nfiles=None):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    nfiles : int, defaults to None
        If provided, also wait for the expected number of files.

    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in directory:
            if fname.endswith('.crdownload'):
                dl_wait = True

        seconds += 1
    return seconds


# In[9]:


def Download_Pdf(profilelinks,download_folder):
    for i in tqdm(profilelinks):
        driver.get(i)
        m = driver.find_element_by_class_name("flex-1")
        m.find_element_by_class_name("pv-s-profile-actions__overflow").click()
        p_name = driver.find_element_by_css_selector('.inline').text
        name = p_name.split(',')[0]
        m.find_element_by_class_name('pv-s-profile-actions--save-to-pdf').click()
        time.sleep(randrange(5, 10))
        filename = max(glob.iglob(download_folder +'/*'), key=os.path.getmtime)
        shutil.move(filename,os.path.join(download_folder, name + '.pdf'))
        download_wait(download_folder, 20)
        print(name)


# In[10]:


if __name__ == '__main__':
    download_folder = "C:\\Users\\Bhagya\\Resume Analyzer\\ACTUAL PROJECT\\resumes"
    driver = Driver_Properties(download_folder)
    Linkedin_Login(Username,Password)
    role = sys.argv[1]
    print(role)
    Search_Role(role)
    location = sys.argv[2]
    print(location)                             #"Orange County, California Area" 
    Filter_Location(location)
    page_limit = int(sys.argv[3])
    page_urls = Get_Page_Urls(page_limit)
    profilelinks = Profile_Links(page_urls)
    Download_Pdf(profilelinks,download_folder)
    driver.close()

