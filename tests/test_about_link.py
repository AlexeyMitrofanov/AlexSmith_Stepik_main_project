import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import Login_page
from pages.main_page import Main_page


@allure.description("Test about link")
def test_about_link():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("Start test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish test")
