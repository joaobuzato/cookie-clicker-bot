from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='../chromedriver')

driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_id('cookie')
store_items = driver.find_elements_by_css_selector('#store div')
game_is_on = True
timeout = time.time() + 3
while game_is_on:

    cookie.click()
    time.sleep(0.00001)
    if time.time() > timeout:
        store_items = driver.find_elements_by_css_selector('#store div')
        for item in store_items[::-1]:
            _class = item.get_attribute('class')
            if _class != 'grayed':
                item.click()
                break
        timeout = time.time() + 3
