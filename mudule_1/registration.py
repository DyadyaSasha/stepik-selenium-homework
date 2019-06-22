def test_0():

    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/registration2.html")

    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    try:
        input_first_name = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.container > form > div.first_block > div.form-group.first_class > input"
        )
        input_first_name.send_keys("q")
    except NoSuchElementException:
        print("Error in first name input")

    try:
        input_second_name = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.container > form > div.first_block > div.form-group.second_class > input"
        )
        input_second_name.send_keys("w")
    except NoSuchElementException:
        # вылетит на url-е: http://suninjuly.github.io/registration2.html
        print("Error in second name input")

    try:
        input_email = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.container > form > div.first_block > div.form-group.third_class > input"
        )
        input_email.send_keys("q@mail.ru")
    except NoSuchElementException:
        print("Error in email input")

    try:
        input_mobile = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.container > form > div.second_block > div.form-group.first_class > input"
        )
        input_mobile.send_keys("88005553535")
    except NoSuchElementException:
        print("Error in mobile input")

    try:
        input_address = driver.find_element(
            By.CSS_SELECTOR,
            "body > div.container > form > div.second_block > div.form-group.second_class > input"
        )
        input_address.send_keys("qqqqq qq")
    except NoSuchElementException:
        print("Error in address input")

    btn = driver.find_element(
        By.CSS_SELECTOR,
        "body > div.container > form > button"
    )
    btn.click()

    import time
    time.sleep(2)

    welcome_text_elt = driver.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    driver.quit()

    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text


if __name__ == '__main__':
    test_0()
