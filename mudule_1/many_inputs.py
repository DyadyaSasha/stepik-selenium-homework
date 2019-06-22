def test_0():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time
    import os


    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/huge_form.html")

    inputs = driver.find_elements(By.CSS_SELECTOR, "body > div.container > form > div > input")

    for input in inputs:
        input.send_keys("q")

    btn = driver.find_element(By.CSS_SELECTOR, "body > div.container > form > button")

    btn.click()

    time.sleep(5)

    alert = driver.switch_to.alert

    text_alert = alert.text

    print(text_alert)

    alert.accept()

    driver.quit()


if __name__ == '__main__':
    test_0()



