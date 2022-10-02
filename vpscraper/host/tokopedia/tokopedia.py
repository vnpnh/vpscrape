from selenium.webdriver.common.by import By

from vpscraper.client import Client
from dataclasses import dataclass


@dataclass
class URL:
    base_url: str = "https://www.tokopedia.com/"
    login_url: str = "https://www.tokopedia.com/login"


class Tokopedia(Client, URL):

    def login(self, email: str, password: str):
        self.driver.get(URL.login_url)
        self.get_element_until_presence(By.ID, 'email-phone').send_keys(email)
        self.get_element_until_presence(By.ID, 'email-phone-submit').click()

        if self.check_element(By.XPATH, '/html/body/div[3]/div[2]/h4'):
            print("Email belum terdaftar")
            return False

        self.get_element_until_presence(By.ID, 'password-input').send_keys(password)

        self.get_element_until_presence(By.XPATH, '//*[@id="zeus-root"]/div/div[2]/section/div['
                                   '2]/form/button').click()

        current_url = self.current_url()
        if self.check_element(By.XPATH, '/html/body/div[4]/div[2]/h4') and current_url == URL.login_url:
            print("Email atau password salah")
            return False
        elif current_url == URL.login_url:
            print("Permintaanmu gagal diproses")


if __name__ == "__main__":
    client = Tokopedia(browser="chrome")
    client.login("waretifyid@gmail.com", password="NoBanned@2022")
