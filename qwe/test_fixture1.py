from selenium import webdriver
import os

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    # метод, который выполнится перед запуском тестов в данном классе
    @classmethod
    def setup_class(cls):
        print("\nstart browser for test suite..")
        cls.browser = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    # метод, который выполнится полсле работы тестов в данном классе
    @classmethod
    def teardown_class(cls):
        print("quit browser for test suite..")
        cls.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    # метод, который выполнится перед каждым запуском теста в данном классе
    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))

    # метод, который выполнится после каждого запуска теста в данном классе
    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

