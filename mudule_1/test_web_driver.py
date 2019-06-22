def test_0():
    from selenium import webdriver
    import time
    import os

    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("https://stepik.org/lesson/25969/step/8")

    time.sleep(5)

    text_area = driver.find_element_by_css_selector(".textarea")

    text_area.send_keys("get()")

    time.sleep(5)

    submit_button = driver.find_element_by_css_selector(".submit-submission")

    submit_button.click()

    time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    test_0()