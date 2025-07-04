from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_details = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for time in event_date:
    print(time.text)
for event in event_details:
    print(event.text)
events = {}
for n in range(len(event_date)):
    events[n] = {
        "time": event_date[n].text,
        "event": event_details[n].text
    }

print(events)