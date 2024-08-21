from typing import Any, Dict

from selenium.webdriver.common.by import By

from vpscraper.config import Config
from vpscraper.consts.shopee import Consts
from vpscraper.host.shopee.base import Shopee
from vpscraper.host.shopee.url import SellerURL


class Seller(Shopee):


    def get_all_products(self, sort_by: str = Consts.TEXT_POPULER) -> dict[str, dict[str, Any]]:
        self.get(SellerURL.seller_product_list_all)
        products = self.find_elements(By.TAG_NAME, "tr", 5)
        items = dict()
        item_info = dict()
        header_flag = True
        for index, product in enumerate(products):
            if index == 0:
                continue
            # if header_flag:
            #     item_info = self._extract_product_list_header(product.text)
            #     if item_info.keys():
            #         header_flag = False
            #         continue

            ID = self.get_product_id()
            print(ID)

            items[ID] = self._extract_product_info(product.text, 'as')

        return items

    def update_product_stock(self, product_id: str):
        pass

    def update_product_variation(self, product_id: str):
        pass

    def update_product_grosir(self):
        pass

    def get_product_id(self, by: str = By.CLASS_NAME, value: str = 'shopee-checkbox__input', wait: int = 0) -> str:
        #TODO still didnt get product id
        return self.find_element(by, value, wait).get_attribute('value')

    def _extract_product_info(self, text: str, link: str) -> dict[str, Any]:
        text = text.split('\n')
        return {
            'title': text[0],
            'code_variant': text[1],
            'variant': text[2],
            'price': text[3],
            'stock': text[4],
            'sold_item': text[5]
        }

    @classmethod
    def _extract_product_list_header(cls, text):
        text = text.split('\n')
        return {str(i): '' for i in text}
