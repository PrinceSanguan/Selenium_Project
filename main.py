from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the service and driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://www.facebook.com/")

# Wait for the login page to load
driver.implicitly_wait(30)

# Find the username and password input fields and fill them in
username_field = driver.find_element(By.NAME, "email")
password_field = driver.find_element(By.NAME, "pass")

username_field.send_keys("carolcorpuz09@yahoo.com")
password_field.send_keys("password")

# Submit the form
password_field.send_keys(Keys.ENTER)

# Wait to see the result
time.sleep(10)

# Close the browser
driver.quit()