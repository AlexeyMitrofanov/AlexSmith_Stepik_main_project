from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):  # Создали класс Main_page

    def __init__(self, driver):  # передаем драйвер чтобы мы могли совершать шаги по авторизации
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы элементов на странице авторизации

    select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    select_product_3 = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart = "//div[@id='shopping_cart_container']"
    burger_menu = "//button[@id='react-burger-menu-btn']"
    about_button = "//a[@id='about_sidebar_link']"

    # Getters - поиск локаторов на странице (эти методы возвращают найденные элементы)

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))

    # Actions - действия которые мы будем делать с локаторами

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select Product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select Product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click select Product 3")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print("Click burger menu")

    def click_about_button(self):
        self.get_about_button().click()
        print("Click about button")

    # Methods - методы, которые будем выполнять

    def select_products_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_burger_menu()
        self.click_about_button()
        self.assert_url("https://saucelabs.com/")
