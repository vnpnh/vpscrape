from vpscraper.host.shopee.base import Shopee
from vpscraper.utils import catch_exception

if __name__ == "__main__":
    shopee = Shopee(browser="chrome")

    @catch_exception
    def run():
        shopee.get("https://shopee.co.id/wantostore95")
        product_info = shopee.get_all_category()
        print(product_info)
        shopee.close()

    run()
