from .notifications import NotificationHandler
from .insta import Insta
from .logger import Logger
from .data import Data


class Notify:
    def __init__(self, username: str, password: str):
        Data.logger = Logger("notification")
        Data.nh = NotificationHandler()
        self.insta = Insta(username, password)

    def send_notification(self, message):
        Data.nh.send_notification(message)

    def upload_image(self, path, description):
        # upload instagram bot
        self.insta.upload_post(path, description)

        # upload notification channels
        Data.nh.send_notification(description, path)

    def upload_story(self, path):
        self.insta.upload_post(path)