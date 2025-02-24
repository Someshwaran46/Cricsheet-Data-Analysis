import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure the download folder
download_folder = "Specific JSON Downloads"
os.makedirs(download_folder, exist_ok=True)

# Set up Selenium WebDriver options for headless browsing
chrome_options = Options()

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# URL of the page to scrape
url = "https://cricsheet.org/matches/"

# Open the webpage
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

# Match types to download (under <dt> tag)
match_types = ["One-day internationals", "T20 internationals", "Test matches", "Indian Premier League"]

# Find all <dt> elements
dt_elements = driver.find_elements(By.TAG_NAME, "dt")

# Loop through <dt> elements and check if they match required types
for dt in dt_elements:
    match_text = dt.text.strip()
    
    if match_text in match_types:
        # Find the next <dd> sibling containing the JSON link
        dd = dt.find_element(By.XPATH, "following-sibling::dd[1]")
        json_link = dd.find_element(By.TAG_NAME, "a").get_attribute("href")

        # Download the JSON file
        response = requests.get(json_link)
        
        if response.status_code == 200:
            file_name = os.path.join(download_folder, json_link.split("/")[-1])
            
            with open(file_name, 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download: {json_link}")

# Close the browser
driver.quit()
