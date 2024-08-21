from vpscraper.host.shopee.seller import Seller

if __name__ == "__main__":
    shopee = Seller(browser="chrome")
    try:
        product_info = shopee.get_all_products()
        print(product_info)

    except Exception as e:
        print(e)
