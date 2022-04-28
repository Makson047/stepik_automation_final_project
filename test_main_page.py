import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    LINK = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.should_be_login_link()     # выполняем метод страницы — переходим на страницу логина


