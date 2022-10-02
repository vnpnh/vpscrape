from abc import abstractmethod

from vpscraper.client import Client


class Ecommerce(Client):

    @abstractmethod
    def login(self, login_key: str, password: str):
        """Ecommerce Login"""
        pass

    @abstractmethod
    def login_phone_number(self, number: str, password: str):
        pass

    @abstractmethod
    def get_product_info(self) -> dict[str, any]:
        pass
