def test_0():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import os
    import time

    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/find_xpath_form")

    inputs = driver.find_elements(By.CSS_SELECTOR, "body > div.container > form > div > input")

    for input in inputs:
        input.send_keys("q")

    btn = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/button[3]")

    btn.click()

    alert = driver.switch_to.alert

    print(alert.text)

    alert.accept()

    driver.quit()


if __name__ == '__main__':
    test_0()