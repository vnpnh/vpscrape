from selenium.webdriver.common.by import By

from vpscraper.host.shopee.base import Shopee
from vpscraper.host.shopee.url import SellerURL


class Seller(Shopee):
    def get_all_products(self):
        self.get(SellerURL.seller_product_list_all)
        data = self.get_element_until_presence(By.NAME, "input")
        print(data)
        print(data.text)
        data = self.get_element_until_presence(By.TAG_NAME, "tr")
        print("aasd ", data.text)

    def update_product_stock(self, product_id: str):
        pass

    def update_product_variation(self, product_id: str):
        pass

    def update_product_grosir(self):
        pass
