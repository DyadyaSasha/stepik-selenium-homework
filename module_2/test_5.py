def test_0():

    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/file_input.html")

    from selenium.webdriver.common.by import By
    driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div > input:nth-child(2)").send_keys("Alex")
    driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div > input:nth-child(4)").send_keys("AlexEEE")
    driver.find_element(By.CSS_SELECTOR, "body > div.container > form > div > input:nth-child(6)").send_keys("Alex@")
    # прикрепляем файл
    driver.find_element(By.CSS_SELECTOR, "#file").send_keys(os.path.join(os.getcwd(), "test.txt"))
    driver.find_element(By.CSS_SELECTOR, "body > div.container > form > button").click()

    print(driver.switch_to.alert.text)

    driver.quit()


if __name__ == '__main__':
    test_0()

