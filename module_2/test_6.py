def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))

def test_0():

    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/alert_accept.html")

    from selenium.webdriver.common.by import By
    driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

    driver.switch_to.alert.accept()

    import time
    time.sleep(1)

    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)

    result = calc(x)

    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)

    driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

    print(driver.switch_to.alert.text)

    driver.quit()


if __name__ == '__main__':
    test_0()
