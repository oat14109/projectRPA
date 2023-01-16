from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Start a web driver (e.g. Chrome)
driver = webdriver.Chrome('path/to/webdriver')

# Navigate to the Google website
driver.get("https://www.google.com/")

# Find the search box element and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium python")

# Find the search button element and click it
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK")))
search_button.click()


# Wait for the search results to load
driver.implicitly_wait(10) # seconds

# Find the first search result link and click it
first_result = driver.find_element(By.XPATH,"//h3/a")
first_result.click()

# Close the web driver
driver.close()