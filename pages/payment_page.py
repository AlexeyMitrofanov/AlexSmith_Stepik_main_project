from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Payment_page(Base):  # Создали класс Payment_page

    def __init__(self, driver):  # передаем драйвер чтобы мы могли совершать шаги по авторизации
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы элементов на странице авторизации

    finish_button = "//button[@id='finish']"

    # Getters - поиск локаторов на странице (эти методы возвращают найденные элементы)

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions - действия которые мы будем делать с локаторами

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    # Methods - методы, которые будем выполнять

    def payment(self):
        Logger.add_start_step(method="payment")
        self.get_current_url()
        self.click_finish_button()
        Logger.add_end_step(url=self.driver.current_url, method="payment")
