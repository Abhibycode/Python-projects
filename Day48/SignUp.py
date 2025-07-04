from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Abhishek", Keys.TAB)

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Kongari", Keys.TAB)

email = driver.find_element(By.NAME, value="email")
email.send_keys("abhikongari123@gmail.com", Keys.TAB)

button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.send_keys(Keys.ENTER)

driver.close()