from typing import Any

from selenium.webdriver.common.by import By
from time import sleep

from vpscraper.base import Ecommerce
from vpscraper.config import Config
from vpscraper.host.shopee.url import ShopeeURL
from vpscraper.consts.shopee import Consts

from vpscraper.host.shopee.utils import extract_rating_info, extract_url


class Shopee(Ecommerce):
    def __init__(self, browser, config: Config):
        super().__init__(browser=browser)
        self.config = config

    def get_phone_number_config(self):
        return self.config.get(Consts.CONFIG_SHOPEE, Consts.CONFIG_PHONE_NUMBER)

    def get_password_config(self):
        return self.config.get(Consts.CONFIG_SHOPEE, Consts.CONFIG_PASSWORD)

    def login(self, login_key: str, password: str):
        self.get(ShopeeURL.LOGIN)
        self.get_element_until_presence(By.NAME, Consts.LOGIN_KEY).send_keys(login_key)
        self.get_element_until_presence(By.NAME, Consts.LOGIN_PASSWORD).send_keys(password)
        self.get_element_until_presence(By.XPATH, Consts.LOGIN_SUBMIT_BUTTON).click()

    def login_phone_number(self, number: str = "", password: str = ""):
        if number == "":
            number = self.get_phone_number_config()

        if password == "":
            password = self.get_password_config()

        self.login(number, password)
        self.get_element_until_presence(By.XPATH, Consts.LOGIN_PAGE_PHONE_NUMBER_BUTTON_1).click()
        self.get_element_until_presence(By.XPATH, Consts.LOGIN_PAGE_PHONE_NUMBER_BUTTON_2).click()
        element = self.get_element_until_presence(By.XPATH, Consts.LOGIN_PAGE_PHONE_NUMBER_OTP_TEXT)
        if element is not None:
            if element.text == Consts.LOGIN_PAGE_PHONE_NUMBER_OTP_TEXT_EXPECTED:
                index = 0
                while True:
                    if self.current_url() != ShopeeURL.VERIFY_LOGIN:
                        break
                    if index == 65:
                        # resend link every 65 seconds
                        self.get_element_until_presence(By.XPATH, Consts.LOGIN_PHONE_NUMBER_RESEND).click()

                    index += 1
                    sleep(1)

    def store_info(self):
        store_info = self.find_element(By.CLASS_NAME, Consts.CLASS_STORE_INFO, 10)
        return self._extract_store_info(store_info.text)

    def get_all_products(self, sort_by: str = Consts.TEXT_POPULER) -> dict[int, dict[str, Any]]:
        self.get_sort_by_page(sort_by)
        total = self.get_total_page(wait=10)
        total_product = 0
        items = dict()
        for i in range(int(total)):
            print("Current Page: ", self.get_current_page(wait=10))
            products = self.find_elements(By.CLASS_NAME, Consts.CLASS_ALL_PRODUCTS, 1)
            for index, product in enumerate(products):
                info = product.find_element(By.TAG_NAME, Consts.A_TAG)
                info = self._extract_product_info(info.text, info.get_attribute(Consts.HREF))
                if info.get('status') != 'habis':
                    items[total_product] = info
                    total_product += 1
            self.next_page(wait=10)
        return items

    def get_product_info(self) -> dict[str, Any]:
        return {
            'title': self.get_title(wait=10),
            'rating': self.get_rating(),
            'score': self.get_score(),
            'sold_out': self.get_sold_out(),
            'discount_price': self.get_discount_price(),
            'current_price': self.get_current_price(),
            'discount': self.get_discount(),
            'stock': self.get_stock(),
            'favorite': self.get_favorite(),
            'specification': self.get_specification(),
            'description': self.get_description(),
            'rating_info': self.get_rating_info(),
            'images': self.get_images()
        }

    def get_all_category(self):
        category = dict()

        categories = self.find_elements(By.CLASS_NAME, Consts.CLASS_CATEGORY, 10)
        for i in categories:
            category[i.text] = i

        return category

    def get_title(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_TITLE, wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_rating(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_RATING, wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_score(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_SCORE, wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_sold_out(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_SOLD_OUT, wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_discount_price(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_DISCOUNT_PRICE,
                           wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_current_price(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_CURRENT_PRICE,
                          wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_discount(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_DISCOUNT, wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_stock(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_STOCK, wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_favorite(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_FAVORITE, wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_specification(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_SPECIFICATION,
                          wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_description(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_DESCRIPTION,
                        wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_rating_info(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PRODUCT_RATING_INFO, wait: int = 0) -> \
            dict[str, str]:
        return extract_rating_info(self.get_element_until_presence(by, value, wait).text)

    def get_images(self) -> dict[int, str]:
        highlight_image = extract_url(
            self.find_element(By.CLASS_NAME, Consts.CLASS_PRODUCT_HIGHLIGHT_IMAGE).get_attribute(Consts.STYLE))
        images_dict = {
            0: highlight_image,
        }

        images = self.find_elements(By.CLASS_NAME, Consts.CLASS_PRODUCT_IMAGES)
        for index, image in enumerate(images):
            images_dict[index + 1] = extract_url(
                image.find_element(By.CLASS_NAME, Consts.CLASS_PRODUCT_IMAGE).get_attribute(Consts.STYLE))
        return images_dict

    def get_current_page(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_CURRENT_PAGE,
                         wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def get_total_page(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_TOTAL_PAGE,
                       wait: int = 0) -> str:
        return self.get_element_until_presence(by, value, wait).text

    def next_page(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_NEXT_PAGE,
                  wait: int = 0):
        self.get_element_until_presence(by, value, wait).click()

    def previous_page(self, by: str = By.CLASS_NAME, value: str = Consts.CLASS_PREVIOUS_PAGE,
                      wait: int = 0):
        self.get_element_until_presence(by, value, wait).click()

    def get_sort_by_page(self, sort_by: str):
        match sort_by:
            case Consts.TEXT_POPULER:
                self.get_element_until_presence(By.XPATH, Consts.XPATH_SORT_BY_PRODUCT_POPULER, 10).click()
            case Consts.TEXT_TERBARU:
                self.get_element_until_presence(By.XPATH, Consts.XPATH_SORT_BY_PRODUCT_TERBARU, 10).click()
            case Consts.TEXT_TERLARIS:
                self.get_element_until_presence(By.XPATH, Consts.XPATH_SORT_BY_PRODUCT_TERLARIS, 10).click()

    @classmethod
    def _extract_product_info(cls, text: str, link: str) -> dict[str, Any]:
        text = text.split("\n")
        return {
            'title': text[3],
            'link': link,
            'status': text[0],
            'discount_percentage': text[1],
            'normal_price': text[-4],
            'current_price': text[-3],
            'sold_out': text[-2],
            'city': text[-1]
        }

    @classmethod
    def _extract_store_info(cls, text):
        text = text.split("\n")
        return {
            'type': text[0],
            'store_name': text[1],
            'total_product': text[4].split(':')[1].strip(),
            'following': text[5].split(':')[1].strip(),
            'chat_performance': text[6].split(':')[1].strip(),
            'followers': text[7].split(':')[1].strip(),
            'score': text[8].split(':')[1].strip(),
            'joined': text[9].split(':')[1].strip(),
        }
