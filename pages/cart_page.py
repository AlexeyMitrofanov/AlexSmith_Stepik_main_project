from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):  # Создали класс Cart_page

    def __init__(self, driver):  # передаем драйвер чтобы мы могли совершать шаги по авторизации
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы элементов на странице авторизации

    checkout_button = "//button[@id='checkout']"

    # Getters - поиск локаторов на странице (эти методы возвращают найденные элементы)

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions - действия которые мы будем делать с локаторами

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods - методы, которые будем выполнять

    def product_confirmation(self):
        Logger.add_start_step(method="product_confirmation")
        self.get_current_url()
        self.click_checkout_button()
        Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")
