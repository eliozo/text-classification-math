from selenium import webdriver
import time

# webdriver_path = 'C:\\Tools\\geckodriver-v0.34.0-win32\\geckodriver.exe'

driver = webdriver.Firefox()

# Navigate to the URL
with open('all_problems.txt', 'r', encoding='utf-8') as file:
    for line in file:
        year, url = line.strip().split(',')
        # url = 'https://artofproblemsolving.com/community/c3080392_2021_isl'
        driver.get(url)
        time.sleep(5)

        # Get the HTML content of the page
        html_content = driver.page_source

        # Save the HTML content to a file
        output_file = 'html/page_{}.html'.format(year)
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(html_content)

        # Close the browser
        # driver.quit()
