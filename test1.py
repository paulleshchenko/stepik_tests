from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn = browser.find_element(By.CSS_SELECTOR, 'button#book.btn')
    btn.click()

    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(x)

    pole_otv = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    pole_otv.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, "button#solve.btn")
    button1.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
