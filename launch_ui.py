from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open the webpage
    url = "https://hashtagbasketball.com/fantasy-basketball-projections"
    driver.get(url)

    # Step 2: Allow manual interaction with the page
    print("You have 60 seconds to manually interact with the page and adjust the settings.")
    time.sleep(30)  # Allow 60 seconds for manual interaction

    print("You have 30 seconds to manually interact with the page and adjust the settings.")
    time.sleep(30)  # Allow 60 seconds for manual interaction
    # Step 3: Save the page source to an HTML file
    page_source = driver.page_source

    # Saving to a file on your computer
    with open("fantasy_basketball_projections.html", "w", encoding="utf-8") as file:
        file.write(page_source)

    print("Page source saved successfully as 'fantasy_basketball_projections.html'.")

finally:
    # Close the driver
    driver.quit()
