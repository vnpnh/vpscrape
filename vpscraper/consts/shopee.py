class Consts:
    CONFIG_SHOPEE: str = 'SHOPEE'
    CONFIG_PHONE_NUMBER: str = 'phone_number'
    CONFIG_PASSWORD: str = 'password'

    LOGIN_KEY: str = 'loginKey'
    LOGIN_PASSWORD: str = 'password'
    LOGIN_SUBMIT_BUTTON: str = '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button'

    LOGIN_PHONE_NUMBER_RESEND: str = '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/button'
    LOGIN_PAGE_PHONE_NUMBER_OTP_TEXT: str = '//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div'
    LOGIN_PAGE_PHONE_NUMBER_OTP_TEXT_EXPECTED: str = 'Respon melalui handphone-mu'
    LOGIN_PAGE_PHONE_NUMBER_BUTTON_1: str = '//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button/div[2]'
    LOGIN_PAGE_PHONE_NUMBER_BUTTON_2: str = '//*[@id="modal"]/aside/div[1]/div/div[2]/button[1]'

    XPATH_SORT_BY_PRODUCT_POPULER: str = '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[' \
                                         '2]/div/div[1]/div[1]/div[1]'
    XPATH_SORT_BY_PRODUCT_TERBARU: str = '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[' \
                                         '2]/div/div[' \
                                         '1]/div[1]/div[2]'
    XPATH_SORT_BY_PRODUCT_TERLARIS: str = '//*[@id="main"]/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[' \
                                          '2]/div/div[1]/div[1]/div[3]'

    TEXT_POPULER: str = 'terbaru'
    TEXT_TERBARU: str = 'terbaru'
    TEXT_TERLARIS: str = 'terbaru'

    CLASS_CATEGORY: str = '_3mieT7'

    CLASS_STORE_INFO: str = 'shop-page__info'

    CLASS_PRODUCT_TITLE: str = '_2rQP1z'
    CLASS_PRODUCT_RATING: str = '_14izon'
    CLASS_PRODUCT_SCORE: str = '_3y5XOB'
    CLASS_PRODUCT_SOLD_OUT: str = 'HmRxgn'
    CLASS_PRODUCT_DISCOUNT_PRICE: str = '_2yjfFH'
    CLASS_PRODUCT_CURRENT_PRICE: str = '_2Shl1j'
    CLASS_PRODUCT_DISCOUNT: str = '_3PlIlX'
    CLASS_PRODUCT_STOCK: str = '_283ldj'
    CLASS_PRODUCT_FAVORITE: str = '_1ipVhx'
    CLASS_PRODUCT_SPECIFICATION: str = '_2jz573'
    CLASS_PRODUCT_DESCRIPTION: str = '_1MqcWX'
    CLASS_PRODUCT_RATING_INFO: str = 'product-rating-overview'
    CLASS_PRODUCT_HIGHLIGHT_IMAGE: str = '_3DKwBj'
    CLASS_PRODUCT_IMAGES: str = '_2Qq8-9'
    CLASS_PRODUCT_IMAGE: str = '_3DKwBj'

    CLASS_CURRENT_PAGE: str = 'shopee-mini-page-controller__current'
    CLASS_TOTAL_PAGE: str = 'shopee-mini-page-controller__total'
    CLASS_NEXT_PAGE: str = 'shopee-icon-button--right'
    CLASS_PREVIOUS_PAGE: str = 'shopee-icon-button--left'

    CLASS_ALL_PRODUCTS: str = 'col-xs-2-4'

    STYLE: str = 'style'
    HREF: str = 'href'
    A_TAG: str = 'a'
