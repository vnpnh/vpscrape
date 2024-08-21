import warnings

from selenium.webdriver.common.by import By

from vpscraper.client import Client
from dataclasses import dataclass

from vpscraper.config import Config
from vpscraper.consts.base import Consts, TokopediaInput


@dataclass
class URL:
    base_url: str = "https://www.tokopedia.com/"
    login_url: str = "https://www.tokopedia.com/login"


class Tokopedia(Client, URL):
    def __init__(self, browser, config: Config):
        if browser != "undetectable-chrome":
            warnings.warn("Some features may not work properly. Please use undetectable-chrome instead.")
        super().__init__(browser=browser)
        self.config = config

    def get_email_config(self):
        return self.config.get(Consts.CONFIG_TOKOPEDIA, Consts.CONFIG_EMAIL)

    def get_password_config(self):
        return self.config.get(Consts.CONFIG_TOKOPEDIA, Consts.CONFIG_PASSWORD)

    def login(self, email: str = "", password: str = ""):
        try:
            email = email or self.get_email_config()
            password = password or self.get_password_config()

            self.driver.get(URL.login_url)

            # Email form
            self.get_element_until_presence(By.NAME, TokopediaInput.EMAIL_INPUT).send_keys(email)
            self.get_element_until_presence(By.CLASS_NAME, TokopediaInput.NEXT_EMAIL_BUTTON).click()

            # Password form
            self.get_element_until_presence(By.CSS_SELECTOR, TokopediaInput.PASSWORD_INPUT).send_keys(password)
            self.get_element_until_presence(By.CLASS_NAME, TokopediaInput.NEXT_EMAIL_BUTTON).click()

            if self._handle_otp_verification():
                print("Login successful.")
                return True

            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def _handle_otp_verification(self) -> bool:
        """Handles OTP verification if required during login."""
        current_url = self.driver.current_url
        while current_url == URL.login_url:
            try:
                otp_input_element = self.get_element_until_presence(By.CSS_SELECTOR, TokopediaInput.OTP_INPUT)
                if otp_input_element:
                    while True:
                        otp = input("Please input OTP (6 digits): ")
                        if len(otp) == 6 and otp.isdigit():
                            print("Entering OTP...")
                            otp_input_element.send_keys(otp)
                            return True
                        else:
                            print("Invalid OTP. Please enter exactly 6 numeric digits.")
                else:
                    print("OTP input field not found. Waiting for the page to load...")
            except Exception as e:
                print(f"An error occurred during OTP verification: {e}")
                return False
            current_url = self.driver.current_url
        return False
