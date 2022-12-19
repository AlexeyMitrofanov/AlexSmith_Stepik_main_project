from base.base_class import Base


class Finish_page(Base):  # Создали класс Finish_page

    def __init__(self, driver):  # передаем драйвер чтобы мы могли совершать шаги по авторизации
        super().__init__(driver)
        self.driver = driver

    # Locators - локаторы элементов на странице авторизации

    # Getters - поиск локаторов на странице (эти методы возвращают найденные элементы)

    # Actions - действия которые мы будем делать с локаторами

    # Methods - методы, которые будем выполнять

    def finish(self):
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        self.screenshot()
