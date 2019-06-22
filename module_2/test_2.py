def test_0():
    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/get_attribute.html")

    from selenium.webdriver.common.by import By
    # get_attribute() для значений атрибутов типа boolean возвращает !строковые! значения ("true"/"false")
    number = int(driver.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex"))

    input = driver.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(calc(number))

    checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    btn = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div > div > button")
    btn.click()

    import time
    time.sleep(2)

    alert = driver.switch_to.alert
    print(alert.text)

    alert.accept()

    driver.quit()


def calc(x):
    import math
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    test_0()
