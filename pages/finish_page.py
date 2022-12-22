import allure

from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):  # Создали класс Finish_page

    def __init__(self, driver):  # передаем драйвер чтобы мы могли совершать шаги по авторизации
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы элементов на странице авторизации

    # Getters - поиск локаторов на странице (эти методы возвращают найденные элементы)

    # Actions - действия которые мы будем делать с локаторами

    # Methods - методы, которые будем выполнять

    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url("https://www.saucedemo.com/checkout-complete.html")
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")
