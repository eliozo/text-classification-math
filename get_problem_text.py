from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Create a Firefox WebDriver
driver = webdriver.Firefox()

# Create a folder to store cleaned HTML
if not os.path.exists("cleaned_html"):
    os.makedirs("cleaned_html")

# Read the URLs from the text file
with open("all_problems.txt", "r") as file:
    urls = file.readlines()

for line in urls:
    year, url = line.strip().split(",")
    year = year.strip()
    url = url.strip()

    # Open the URL
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(5)

    # Find all div elements with class 'cmty-view-post-item-text'
    div_elements = driver.find_elements(By.XPATH, "//div[@class='cmty-view-post-item-text']")

    # Initialize selected_text to store the text from all div elements
    selected_text = ""

    # Select the text within each div element
    for div_element in div_elements:
        # Select the text within the div element
        driver.execute_script(
            "var range = document.createRange(); range.selectNode(arguments[0]); window.getSelection().removeAllRanges(); "
            "window.getSelection().addRange(range);",
            div_element)

        # Copy the selected text
        text = driver.execute_script("return window.getSelection().toString();")

        # Add the selected text to selected_text
        selected_text += text + "\n"

    # Save the selected text to a file
    with open(f"cleaned_html/{year}_cleaned_text.txt", "w", encoding="utf-8") as file:
        file.write(selected_text)

# Close the WebDriver
driver.quit()