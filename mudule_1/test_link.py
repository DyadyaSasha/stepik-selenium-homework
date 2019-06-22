


def test_0():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import math
    import os
    import time

    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/find_link_text")

    s = str(math.ceil(math.pow(math.pi, math.e)*10000))

    link = driver.find_element(By.PARTIAL_LINK_TEXT, s)

    link.click()

    input_first_name = driver.find_elements_by_css_selector("body > div.container > form > div > input")

    keys = ["Ivan", "Petrov", "Smolensk", "Russia"]

    for index in range(len(keys)):
        input_first_name[index].send_keys(keys[index])

    submit_btn = driver.find_element_by_css_selector("body > div.container > form > button")

    submit_btn.click()

    import time
    time.sleep(10)

    alert = driver.switch_to.alert

    text_alert = alert.text

    print(text_alert)

    alert.accept()

    time.sleep(5)

    driver.quit()


if __name__ == '__main__':
    test_0()