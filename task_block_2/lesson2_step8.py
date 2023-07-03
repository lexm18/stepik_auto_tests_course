from typing import Callable, Any, Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

from selenium.webdriver.remote.webelement import WebElement
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить данные: фамилия, имя, адрес эл.почты
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.test")

    # Нажать кнопку "Выбирите файл"
    type = browser.find_element(By.ID, "file")
    send_keys: Callable[[Any, Optional[Any]], WebElement] = browser.find_element

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'l2s8.txt')  # добавляем к этому пути имя файла
    type.send_keys(file_path)  # отправить файл

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()