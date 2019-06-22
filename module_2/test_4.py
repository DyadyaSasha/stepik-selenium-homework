def calc(x):
    import math
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_0():

    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("https://suninjuly.github.io/execute_script.html")

    from selenium.webdriver.common.by import By
    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)

    result = calc(x)
    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)

    driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    # выполняем скрипт JS : прокручивается вниз страница
    # в webdriver нужно использовать return в вызове скрипта (При этом при тестировании скрипта в консоли браузера слово return использовать не надо)
    # driver.execute_script("return arguments[0].scrollIntoView(true);",
    #                       driver.find_element(By.CSS_SELECTOR, "body > div.container > form > button"))

    driver.execute_script("window.scrollBy(0, 100);")

    driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    driver.find_element(By.CSS_SELECTOR, "body > div.container > form > button").click()

    alert = driver.switch_to.alert

    print(alert.text)

    driver.quit()


if __name__ == '__main__':
    test_0()
