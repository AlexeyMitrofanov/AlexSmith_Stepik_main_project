import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@pytest.mark.run(order=2)
def test_buy_product_1(set_up, set_group):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("Start test 1")

    login = Login_page(driver)  # Создали переменную с экземпляром класса
    login.autorization()

    mp = Main_page(driver)  # Создали переменную с экземпляром класса
    mp.select_products_1()

    cp = Cart_page(driver)  # Создали переменную с экземпляром класса
    cp.product_confirmation()

    cip = Client_information_page(driver)  # Создали переменную с экземпляром класса
    cip.input_information()

    pp = Payment_page(driver)  # Создали переменную с экземпляром класса
    pp.payment()

    fp = Finish_page(driver)  # Создали переменную с экземпляром класса
    fp.finish()

    print("Finish test 1")


@pytest.mark.run(order=3)
def test_buy_product_2(set_up, set_group):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("Start test 2")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.product_confirmation()

    print("Finish test 2")


@pytest.mark.run(order=1)
def test_buy_product_3(set_up, set_group):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("Start test 3")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.product_confirmation()

    print("Finish test 3")