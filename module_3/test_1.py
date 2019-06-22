import pytest

@pytest.fixture(scope="function")
def driver():
    import os
    from selenium import webdriver
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))
    yield driver
    driver.quit()

@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_step(driver, url):
    import time
    import math
    driver.implicitly_wait(12)
    driver.get(url)
    driver.find_element_by_tag_name("textarea").send_keys(str(math.log(int(time.time()))))
    driver.find_element_by_tag_name("button").click()
    assert driver.find_element_by_class_name("smart-hints__hint").text == "Correct!", "smart hint is not correct"