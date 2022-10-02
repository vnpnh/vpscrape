import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from vpscraper.client import Client


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.client = Client(browser="chrome")

    def test_search_in_python_org(self):
        client = self.client
        client.get("http://www.python.org")
        self.assertIn("Python", client.driver.title)
        elem = client.get_element_until_presence(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", client.driver.page_source)

    def tearDown(self):
        self.client.close()


if __name__ == "__main__":
    unittest.main()
