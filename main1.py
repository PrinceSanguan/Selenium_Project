from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup
import time
# import pandas as pd

# Set up the service and driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Get the Website
driver.get("https://ca.indeed.com/")