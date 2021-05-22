from typing import Mapping
from .notifications import NotificationHandler
from .insta import Insta
from .logger import Logger
from .data import Data


class Notify:
    def __init__(self, username: str, password: str):
        self.notification = NotificationHandler()
        self.insta = Insta(username, password)

        Data.nh = self.notification

        self.logger = Logger("notification")

    def send_notification(self, message):
        self.notification.send_notification(message)

    def upload_image(self, path, description):
        # upload instagram bot
        self.insta.upload_post(path, description)

        # upload notification channels
        self.notification.send_notification(description, path)

    def upload_story(self, path):
        self.insta.upload_post(path)