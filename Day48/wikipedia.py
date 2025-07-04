from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_of_articles = driver.find_element(By.CLASS_NAME, value="mp-box li a")
print(num_of_articles.text)

# content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

search_box = driver.find_element(By.NAME, value="search")
search_box.send_keys("Python", Keys.ENTER)