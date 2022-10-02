from vpscraper.host.shopee.base import Shopee

if __name__ == "__main__":
    shopee = Shopee(browser="chrome")
    try:
        shopee.get("https://shopee.co.id/wantostore95")
        product_info = shopee.store_info()
        print(product_info)
        shopee.close()

    except Exception as e:
        print(e)
        shopee.close()
