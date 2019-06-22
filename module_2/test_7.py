def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))


def test_0():

    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/redirect_accept.html")

    from selenium.webdriver.common.by import By
    driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

    # узнаём имя на только что открытую новую вкладку в браузере
    new_window_name = driver.window_handles[1]
    # переключаемся на новую вкладку (и продолжаем работу уже в ней)
    driver.switch_to.window(new_window_name)

    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)

    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))

    driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

    print(driver.switch_to.alert.text)

    driver.quit()


if __name__ == '__main__':
    test_0()