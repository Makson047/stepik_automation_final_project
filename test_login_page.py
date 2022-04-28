from .pages.login_page import LoginPage


LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_can_see_login_link(browser):
    page = LoginPage(browser, LINK)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу
    page.should_be_login_link()         # выполняем метод страницы — проверяем что находимся на странице с авторизацией


def test_login_form_is_present(browser):
    page = LoginPage(browser, LINK)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу
    page.should_be_login_form()         # выполняем метод страницы — проверяем присутствует ли форма логина


def test_register_form_is_present(browser):
    page = LoginPage(browser, LINK)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()                         # открываем страницу
    page.should_be_register_form()      # выполняем метод страницы — проверяем присутствует ли форма регистрации
