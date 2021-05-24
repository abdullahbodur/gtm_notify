# from instabot import Bot
from instagrapi import Client
from instagrapi.exceptions import ClientError, PhotoNotUpload
from os import path, getcwd

from .data import Data
import traceback
import time


jsn = "gtmtrade_uuid_and_cookie.json"

insta_conf_path = f"{path.abspath(getcwd())}/gtm_notify/notify/config/instabot_config/"


class Insta:
    def __init__(self, username: str, password: str):

        self.client = Client()

        while True:
            try:
                self.client.login(username, password)

                print(f"Instagram : Login is Successfuly : {self.client.user_id}")

                break

            except ClientError as e:
                Data.logger.info(e)

            except Exception:
                exc = traceback.format_exc()
                Data.logger.error(exc)
                time.sleep(1)

    def upload_post(self, paths, description):
        """
        it uploads photo as a post to instagram.

        @params :
            - path (str) : image_path
            - description (str) : post description

        @return :
            - None
        """

        for i in range(5):
            try:
                if len(paths) > 1:
                    self.client.album_upload(paths, caption=description)
                if len(paths) == 1:
                    self.client.photo_upload(paths[0], caption=description)

                break
            except Exception:
                exc = traceback.format_exc()
                Data.logger.error(exc)
                time.sleep(1)

    def upload_story(self, path: str):
        """
        it uploads photo as a story to instagram.

        @params :
            - path (str) : image_path

        @return :
            - None
        """

        if path != "":
            while True:

                try:
                    self.client.photo_upload_to_story(path)
                    break

                except PhotoNotUpload as e:
                    Data.logger.info(f"Photo Not Upload {e}")
                    time.sleep(1)

                except Exception:
                    exc = traceback.format_exc()
                    Data.logger.error(exc)
                    break