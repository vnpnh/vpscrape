import os
from dataclasses import dataclass
from os.path import devnull
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

from vpscraper.errors import ClientException
from abc import ABC


@dataclass
class Client(ABC):
    """
    browser: use undetectable-chrome if chrome not working
    """

    browser: str
    driver: webdriver = None
    wait: WebDriverWait = None
    log_path: str = devnull

    def __post_init__(self):
        match self.browser:
            case "firefox":
                options = webdriver.FirefoxOptions()
                options.set_preference('dom.webnotifications.enabled', False)
                options.set_preference('dom.push.enabled', False)
                self.driver = webdriver.Firefox(
                    options=options,
                    service=FirefoxService(GeckoDriverManager().install(), log_path=self.log_path),
               )
            case "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument(f"--user-data-dir={self.get_user_data_dir()}")
                self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(), log_path=self.log_path),
                                               options=options)
            case "edge":
                self.driver = webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager().install(), log_path=self.log_path))
            case "undetectable-chrome":
                options = webdriver.ChromeOptions()
                options.add_argument(f"--user-data-dir={self.get_user_data_dir()}")
                self.driver = uc.Chrome(options=options, use_subprocess=True)
            case _:
                raise ClientException

        self.adjust_time_waiting()

    @classmethod
    def get_user_data_dir(cls) -> str:
        user_home_dir = os.path.expanduser('~')
        return os.path.join(user_home_dir, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default')

    def current_url(self) -> str:
        return self.driver.current_url

    def get(self, url: str):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def check_element(self, by: str, value: str) -> bool:
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def get_element_until_presence(self, by: str, value: str, wait: int = 10) -> webdriver:
        if wait != 10:
            self.adjust_time_waiting(wait)
        return self.wait.until(ec.presence_of_element_located((by, value)))

    def find_element(self, by: str, value: str, wait: int = 0) -> webdriver:
        sleep(wait)
        return self.driver.find_element(by, value)

    def find_elements(self, by: str, value: str, wait: int = 0) -> webdriver:
        sleep(wait)
        return self.driver.find_elements(by, value)

    def adjust_time_waiting(self, wait: int = 10):
        self.wait = WebDriverWait(self.driver, wait)
