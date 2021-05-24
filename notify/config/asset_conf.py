from os import path, getcwd


class AssetConfig:

    ASSET_PATH = path.abspath(getcwd()) + "/gtm_notify/notify/assets/"

    OUT_PATH = ASSET_PATH + "out/"

    IMAGE_PATH = ASSET_PATH + "img/"

    FONT_PATH = ASSET_PATH + "fonts/"

    DEFAULT_FONT = "rubik-m.ttf"

    M_FONT_SIZE = 30

    WHITE = "white"
