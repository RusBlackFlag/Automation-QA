from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elem1 = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input1.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

    # # confirm = browser.switch_to.alert
    # # confirm.accept()
    # first_window = browser.window_handles[0]
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    # x_element = browser.find_element(By.ID, 'input_value')
    # x = x_element.text
    # y = calc(x)
    # input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    # input1.send_keys(y)
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    # input1.send_keys('Cfyz')
    # input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    # input2.send_keys('eee')
    # input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    # input3.send_keys('334@mail.ru')
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_name = "file_example.txt"
    # file_path = os.path.join(current_dir, file_name)
    # element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # element.send_keys(file_path)
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # x_element = browser.find_element(By.ID, 'input_value')
    # x = x_element.text
    # y = calc(x)
    # input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    # input1.send_keys(y)
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # option1 = browser.find_element(By.ID, 'robotCheckbox')
    # option1.click()
    # option2 = browser.find_element(By.ID, 'robotsRule')
    # option2.click()
    # button.click()

    # select = Select(browser.find_element(By.ID, 'dropdown'))
    # select.select_by_value(res)  # ищем элемент с текстом "Python"
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # picture = browser.find_element(By.ID, 'treasure')
    # valuex = picture.get_attribute("valuex")
    # y = calc(valuex)
    # input1 = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    # input1.send_keys(y)
    # option1 = browser.find_element(By.ID, 'robotCheckbox')
    # option1.click()
    # option2 = browser.find_element(By.ID, 'robotsRule')
    # option2.click()
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()