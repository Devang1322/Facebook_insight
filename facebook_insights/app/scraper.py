from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  # Import the Service class
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("user-agent=Your-User-Agent-Here")  

service = Service(executable_path="/Users/devanggupta/Desktop/facebook_insights/chromedriver-mac-arm64/chromedriver") 


driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://www.facebook.com")


email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
email.send_keys("raja123guptas@gmail.com")  # Replace with your email
password.send_keys("Allu@123")       # Replace with your password
password.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Navigate to the Facebook page (boat.lifestyle in this case)
page_url = "https://www.facebook.com/boat.lifestyle"
driver.get(page_url)


time.sleep(5)


content = driver.page_source


soup = BeautifulSoup(content, "html.parser")


title = soup.find("title")
print(f"Page Title: {title.text}")


driver.quit()
