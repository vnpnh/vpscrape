from vpscraper.host.shopee.seller import Seller

if __name__ == "__main__":
    client = Seller(browser="chrome")
    client.login_phone_number("087781863350", password="Corsair10")
    client.get_all_products()