# Scrapper

Web Scraping is a technique used to extract data from websites. Python is the perfect language for web scraping where we find many libraries available to be installed through the Python package manager pip.

In this project we used Selenium Web Driver which is a portable framework for testing web applications. The number of web pages you can scrape on LinkedIn is limited, which is why I will be scraping few number of resumes for training our data.

__Prerequisite Installations__

    pip install selenium
    pip install time
    pip install csv
    
The LinkedIn scraper takes a list of LinkedIn user URLs as an input. It will visit each profile on your behalf and extract every single piece of publicly available data from it.

__Process done in this project:__

1. Logging into home page by passing the credentials in a config file
2. Searching for a required role such as _'Data Scientist'_ as in our project
3. Search for _People_ and filtering Location as _'Orange County, California Area'_ 
4. Navigating to number of pages required
5. Collecting all the URLs of people from the pages and storing in a list
6. Visiting each profile from the URLs and saving their profile in a pdf format
7. Storing all the resumes in our local system by giving the downloadfolder path

__Automating Linkedin Login Home Page__

    # import web driver
    from selenium import webdriver

    # specifies the path to the chromedriver.exe
    driver = webdriver.Chrome('/Users/username/bin/chromedriver')

    # driver.get method() will navigate to a page given by the URL address
    driver.get('https://www.linkedin.com')
    
The driver.get() method will navigate to the LinkedIn website and the WebDriver will wait until the page has fully loaded before another command can be executed. If you have installed everything listed and executed the above lines correctly, the Google Chrome application will open and navigate to the LinkedIn website.

__Logging in by passing username and password__

    username = driver.find_element_by_id('username')
    username.send_keys('xxxx@xxx.com')   #Pass your USERNAME here
    passwd = driver.find_element_by_id('password')
    passwd.send_keys('xxxxxxxx')         #Pass your PASSWORD here
    
Searching for required role, location, Page urls, Profile links and Downloading pdfs are mentioned in the .ipynb file

# Data Cleaning

Extracting data from the resumes downloaded and removing unwanted data. Categorizing data into dataframes and storing in a Comma Separated Values(CSV) file.

__Prerequisite Installations__

        pip install slate3k
        pip install pandas

 __1. slate3k:__ slate is a Python package that simplifies the process of extracting text from PDF files. It depends on the PDFMiner package. Slate provides one class, PDF. PDF takes a file-like object and will extract all text from the document, presentating each page as a string of text.
 
 __2. pandas:__ pandas is a Python package providing fast, flexible, and expressive data structures designed to make working with structured and time series data both easy and intuitive. For data scientists, working with data is typically divided into multiple stages: munging and cleaning data, analyzing / modeling it, then organizing the results of the analysis into a form suitable for plotting or tabular display. pandas is the ideal tool for all of these tasks.

__Importing Packages__
        
        import slate3k as slate
        import pandas as pd
        import warnings
        import re
 
 ### Process done:
 
 1. Replacing unwanted characters with space
 2. Removing punctuation
 3. Filtering people with Masters/PhD degree as we need only those people for a Data Scientist role
 4. Filtering total experience of people and storing in a new column 
 5. Extracting Contact with either Email/github link/Phone number
 6. Creating Candidate name for each of the extracted person information
 7. Reading all the data into csv file
