import configparser

class Config:
    def __init__(self, filename):
        self.config = configparser.ConfigParser()
        self.filename = filename
        self.load_config()

    def load_config(self):
        """Load the configuration file."""
        try:
            with open(self.filename, 'r') as f:
                self.config.read_file(f)
        except FileNotFoundError:
            print(f"Error: The configuration file {self.filename} was not found.")

    def get(self, section, option):
        """Retrieve values from the configuration."""
        try:
            return self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(f"Error: {str(e)}")
            return None

# Usage
if __name__ == "__main__":
    config = Config('config.ini')
    print("Host:", config.get('DEFAULT', 'host'))
    print("Port:", config.get('DEFAULT', 'port'))
    print("Username:", config.get('database', 'username'))
    print("Password:", config.get('database', 'password'))
