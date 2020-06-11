import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

#Chrome

def selenium_webscraping_function(page_url):
    # Initiate the driver for chrome
    driver = webdriver.Chrome()

    # make a get request from the page
    driver.get(page_url)

    # Pass the HTML contents to Beautiful Soup for parsing.
    page_soup = BeautifulSoup(driver.page_source)

    return page_soup

'''
Web Scrapping Notes: 
Good guidelines article for selenium 
https://medium.com/datadriveninvestor/web-scraping-with-python-using-selenium-9a08b85b718a

1. install selenium
pip install selenium 

2. install chromedriver
- Download the drivers from https://sites.google.com/a/chromium.org/chromedriver/downloads
- For MAC: it is better to create a folder in /Users/[username]/Documents/driver
- copy the chromedriver file in the folder, Note: name of the file should be chromedriver
- pip install chromedriver
- Note: It is seen that you need to setup extra permission to launch chromedriver
    Command1: xattr -d com.apple.quarantine <name-of-executable>
    Example: 
    $ xattr -d com.apple.quarantine chromedriver 
    
    (or)
    Command2: spctl --add --label 'Approved' <name-of-executable>
    Source: https://docwhat.org/upgrading-to-catalina

3. Include the chromedriver path in to $PATH
    - Open up Terminal.
    - Run the following command:
        sudo nano /etc/paths
    - Enter your password, when prompted.
    - Go to the bottom of the file, and enter the path you wish to add. in my case, the path was /Users/[username]/Documents/driver
    - Hit control-x to quit.
    - Enter “Y” to save the modified buffer, press enter to exit
    - That’s it!  To test it, in new terminal window, type:
    - echo $PATH to verify your changes
    
********* Ready to use Selenium now ************

'''