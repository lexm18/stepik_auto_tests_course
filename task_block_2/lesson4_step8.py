from typing import Callable, Any, Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Проверка в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    # Нажать кнопку
    button = browser.find_element(By.ID, "book")
    button.click()

    # расчет
    x_element = browser.find_element(By.XPATH, "//span[@class='nowrap' and @id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input:required")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
