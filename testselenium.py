from selenium import webdriver

# Start a web driver (e.g. Chrome)
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.example.com/")

# Find an element on the page by its ID and enter text
driver.find_element_by_id("username").send_keys("myusername")

# Find an element on the page by its name and enter text
driver.find_element_by_name("password").send_keys("mypassword")

# Find a button on the page by its text and click it
driver.find_element_by_xpath("//button[contains(text(), 'Sign In')]").click()

# Wait for a specific element to load on the page
driver.implicitly_wait(10) # seconds

# Find an element on the page by its class name and interact with it
driver.find_element_by_class_name("my-class").click()

# Close the web driver
driver.close()