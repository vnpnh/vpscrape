from vpscraper.config import Config
from vpscraper.host.shopee.seller import Seller

if __name__ == "__main__":
	configs = Config('config.ini')
	client = Seller(browser="chrome", config=configs)
	client.login_phone_number()
	client.get_all_products()
