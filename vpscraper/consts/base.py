from dataclasses import dataclass

@dataclass
class Consts:
    CONFIG_TOKOPEDIA: str = 'TOKOPEDIA'
    CONFIG_EMAIL: str = 'email'
    CONFIG_PASSWORD: str = 'password'
    CONFIG_PHONE: str = 'phone'

@dataclass
class TokopediaInput:
    EMAIL_INPUT: str = 'login'
    NEXT_EMAIL_BUTTON: str = 'css-bp4m37'
    PASSWORD_INPUT: str = 'div.css-vyote input[type="password"]'
    WRONG_CREDENTIALS_LOGIN: str = 'div.css-y0w6gg p'
    OTP_INPUT: str = 'input[aria-label="otp input"]'
