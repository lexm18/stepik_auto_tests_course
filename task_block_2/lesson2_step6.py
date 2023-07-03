from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # расчет
    x_element = browser.find_element(By.XPATH, "//span[@class='nowrap' and @id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input:required")
    input1.send_keys(y)

    # Отметить чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    # Выбрать радиокнопку
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script('return arguments[0].scrollIntoView(true);', option1)
    option1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()