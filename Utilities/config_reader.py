from configparser import ConfigParser


# utility:
def read_config(section, key):
    config = ConfigParser()
    config.read("..\\ConfigData\\config.ini")

    return config.get(section, key)

