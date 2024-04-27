from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL of the webpage
url = "https://artofproblemsolving.com/community/c3080392_2021_isl"

# Create a Firefox WebDriver
driver = webdriver.Firefox()

# Open the URL
driver.get(url)

# Find the element containing the text
# element = driver.find_element_by_xpath("//p[contains(text(), 'example')]")
# div_elements = driver.find_elements(By.TAG_NAME, 'div') - savāc visus div
time.sleep(5)
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
with open("selected_text.txt", "w") as file:
    file.write(selected_text)

# Close the WebDriver
driver.quit()
