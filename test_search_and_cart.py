from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://your-bookstore-url.com")

# Search for a book
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python")
search_box.submit()
sleep(2)

# Add to cart
add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
add_button.click()
sleep(1)

# Go to cart
cart_link = driver.find_element(By.ID, "cart")
cart_link.click()

assert "Python" in driver.page_source

driver.quit()
