from typing import Callable, Any, Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time
import os
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Имя первой вкладки
    first_window = browser.window_handles[0]

    # Нажать кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Имя новой вкладки
    new_window = browser.window_handles[1]

    # Переключиться на новую вкладку
    browser.switch_to.window(new_window)

    # расчет
    x_element = browser.find_element(By.XPATH, "//span[@class='nowrap' and @id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input:required")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()