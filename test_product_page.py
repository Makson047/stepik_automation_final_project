import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.guest
class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    @pytest.mark.parametrize('path', ["0", "1", "2", "3", "4", "5", "6",
                                      pytest.param("7", marks=pytest.mark.xfail),
                                      "8", "9"])
    def test_guest_can_add_product_to_basket(self, browser, path):
        LINK = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{path}"
        page = ProductPage(browser, LINK)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.verify_added_product()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, LINK)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, LINK)
        page.open()
        page.add_product_to_basket()
        page.should_be_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, LINK)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, LINK)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, LINK)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, LINK)
        basket_page.verify_is_basket_empty()


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"
        EMAIL = str(time.time()) + "@fakemail.org"
        PASSWORD = "test_password"

        login_page = LoginPage(browser, LINK)
        login_page.open()
        login_page.register_new_user(EMAIL, PASSWORD)
        login_page.should_be_authorized_user()

    def test_guest_cant_see_success_message(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, LINK)
        page.open()
        page.add_product_to_basket()
        page.verify_added_product()
