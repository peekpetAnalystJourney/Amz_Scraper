"""
An application to scrape amazon.jobs website.
Passing an URL, it will return all the job IDs and job titles found in that URL.
Then, the app will create the job URL for each job found and, finally, will
save all the info in a CSV file.
"""
import re
import sys
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless=new") # for Chrome >= 109
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://duckgo.com"
driver.get(start_url)
print(driver.page_source.encode("utf-8"))
# b'<!DOCTYPE html><html xmlns="http://www....
driver.quit()

