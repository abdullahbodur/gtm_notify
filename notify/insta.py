from instabot import Bot
from .data import Data
import traceback
import time
from os import remove, path, getcwd


jsn = "gtmtrade_uuid_and_cookie.json"

insta_conf_path = f"{path.abspath(getcwd())}/gtm_notify/notify/config/instabot_config/"


class Insta:
    def __init__(self, username: str, password: str):
        # creating an instance bot api
        self.bot = Bot(base_path=insta_conf_path)

        if path.exists(insta_conf_path + jsn):
            remove(insta_conf_path + jsn)

        while True:
            try:
                self.bot.login(username=username, password=password)
                break
            except Exception:
                exc = traceback.format_exc()
                Data.logger.error(exc)
                time.sleep(1)
                pass

    def upload_post(self, path, description):
        """
        it uploads photo as a post to instagram.

        @params :
            - path (str) : image_path
            - description (str) : post description

        @return :
            - None
        """
        try:
            with open(path) as img:
                self.bot.upload_photo(img, caption=description)

        except FileNotFoundError:
            Data.logger.info(f"File Not Found {path} ")

    def upload_story(self, path):
        """
        it uploads photo as a story to instagram.

        @params :
            - path (str) : image_path

        @return :
            - None
        """

        try:
            with open(path) as img:
                self.bot.upload_story_photo(img)

        except FileNotFoundError:
            Data.logger.info(f"File Not Found {path} ")