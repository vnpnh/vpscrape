from vpscraper.host.shopee.base import Shopee

if __name__ == "__main__":
    shopee = Shopee(browser="chrome")
    try:
        shopee.get("https://shopee.co.id/Love-Beauty-Planet-Masker-Bundle-Face-Mask-Murumuru-Coconut-Tea-Tree-21-ML-ISI-3-i.155169027.5682364612?sp_atk=d97fd140-9faa-4dca-a82e-fef31d5bd2cd")
        product_info = shopee.get_product_info()
        print(product_info)
        shopee.close()
    except Exception as e:
        print(e)
        shopee.close()
