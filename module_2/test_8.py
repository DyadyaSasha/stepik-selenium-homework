def calc(x):
    import math
    return str(math.log(abs(12*math.sin(int(x)))))

def test_0():

    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    # неявное ожидание в течение 5 секунд при каждом вызове метода find_element
    # в течение 5 секунд через каждую секунду будет вызываться метод find_element пока не найдётся элемент или не истечёт 5 секунд
    driver.implicitly_wait(5)

    # явное ожидание, пока не удовлетвориться условие, например: пока текст в элементе не станет равным указанному
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "10000 RUR")
    )

    driver.find_element(By.CSS_SELECTOR, "#book").click()

    x = int(driver.find_element(By.CSS_SELECTOR, "#input_value").text)

    driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))

    driver.find_element(By.CSS_SELECTOR, "#solve").click()

    print(driver.switch_to.alert.text)

    driver.quit()


if __name__ == '__main__':
    test_0()
