def test3():

    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/selects1.html")

    from selenium.webdriver.common.by import By
    num_1 = int(driver.find_element(By.CSS_SELECTOR, "#num1").text)
    num_2 = int(driver.find_element(By.CSS_SELECTOR, "#num2").text)

    from selenium.webdriver.support.select import Select
    select = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_visible_text(str(num_1 + num_2))

    driver.find_element(By.CSS_SELECTOR, "body > div.container > form > button").click()

    import time
    time.sleep(4)

    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

    driver.quit()


if __name__ == '__main__':
    test3()