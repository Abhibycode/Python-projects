from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)

bug_link = driver.find_element(By.XPATH, value='//*[@id="homepage"]/script[1]')
print(bug_link.text)

#closes browers
#driver.close()
#closes complete program
driver.quit()