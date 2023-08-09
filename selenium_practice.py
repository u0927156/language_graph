# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# %%
driver.get("https://ilibrary.ru/text/11/p.1/index.html")

# %%


def find_foward_nav_element_ilibrary(driver):
    nav_elements = driver.find_elements(By.CLASS_NAME, "navlink")
    for element in nav_elements:
        element_title = element.get_attribute("title")

        if element_title == "Дальше":
            return element

    return None


while True:
    forward_nav_element = find_foward_nav_element_ilibrary(driver)

    if forward_nav_element is not None:
        forward_nav_element.click()
        time.sleep(1)
    else:
        break


# %%
driver.quit()
# %%
