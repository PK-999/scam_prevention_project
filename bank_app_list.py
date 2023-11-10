from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Define the search phrase
search_phrase = "Your Search Phrase"  # Replace with your desired search phrase

# Initialize Chrome WebDriver (you can use other browsers too)
driver = webdriver.Chrome()

# Open the App Store
driver.get("https://apps.apple.com/us/app/apple-store/id375380948")

# Find the search input field by its name and enter the search phrase
search_box = driver.find_element_by_name("q")
search_box.clear()
search_box.send_keys(search_phrase)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load (you can adjust the sleep time)
time.sleep(5)

# Perform actions on the search results, e.g., scrape data or click on apps

# Close the browser when done
driver.quit()
