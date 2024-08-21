class ShopeeURL:
    BASE: str = "https://shopee.co.id/"
    LOGIN: str = "https://shopee.co.id/buyer/login"
    VERIFY_LOGIN: str = "https://shopee.co.id/verify/link"


class BuyerURL:
    pass


class SellerURL:
    seller_url: str = "https://seller.shopee.co.id/"
    product_url: str = "https://seller.shopee.co.id/portal/product/{}"

    seller_product_list_all: str = "https://seller.shopee.co.id/portal/product/list/all"





