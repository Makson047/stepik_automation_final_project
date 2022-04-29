from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        # проверка на корректный url адрес
        LOGIN_STR = 'login'
        link = self.browser.current_url
        assert LOGIN_STR in link, f'Current link don`t have substring "{LOGIN_STR}"'

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_form.send_keys(email)
        password_form_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        password_form_1.send_keys(password)
        password_form_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        password_form_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
