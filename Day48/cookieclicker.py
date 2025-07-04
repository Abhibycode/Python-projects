from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import time, sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

sleep(3)

print("Language selection")
try:
    prompt_anchor = driver.find_element(By.ID, value="langSelect-EN")
    prompt_anchor.click()
    sleep(3)
except NoSuchElementException:
    print("No Such Element found")

sleep(2)

Not_a_robot = driver.find_element(By.CLASS_NAME, value="cb-c checkbox")
Not_a_robot.click()


items_ids = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60*5

cookie_click = driver.find_element(By.CLASS_NAME, value="bigCookie")

while True:
    cookie_click.click()
    if time() >timeout:
        try:
            cookies_element = driver.find_elements(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))
            products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None

            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except NoSuchElementException:
            print("Couldn't find cookie count or items")


        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            print(f"Final Result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie")

        break