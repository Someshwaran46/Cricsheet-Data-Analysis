import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure the download folder
download_folder = "Web Scrapping Downloads"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)


chrome_options = Options()
chrome_options.add_argument(f"download.default_directory={os.path.abspath(download_folder)}")

# Initialize the WebDriver (ensure the correct path to chromedriver is provided)
driver = webdriver.Chrome(options=chrome_options)

# URL of the page to scrape
url = "https://cricsheet.org/matches/"

# Open the webpage
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

# Find all the links to .json files
json_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'json.zip')]")

# Loop through each link and download the JSON file
for link in json_links:
    json_url = link.get_attribute("href")

    # Download the JSON file using requests
    response = requests.get(json_url)
    
    if response.status_code == 200:
        # Define the file name and path to save the downloaded file
        file_name = os.path.join(download_folder, json_url.split("/")[-1])
        
        # Save the file content to the local file system
        with open(file_name, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {json_url}")
