from vpscraper.config import Config
from vpscraper.host.tokopedia.tokopedia import Tokopedia
configs = Config('config.ini')
client = Tokopedia(browser="undetectable-chrome", config=configs)
client.login()
