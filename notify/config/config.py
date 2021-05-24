from os import path, getcwd


class Config:
    CONFIG_PATH = f"{path.abspath(getcwd())}/gtm_notify/notify/config/"

    APPRISE_CONFIG_PATH = CONFIG_PATH + "apprise.yml"
