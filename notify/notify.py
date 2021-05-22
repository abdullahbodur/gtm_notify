from .notifications import NotificationHandler
from .insta import Insta


class Notify:
    def __init__(self, username: str, password: str, logger):
        self.notification = NotificationHandler()
        self.insta = Insta(username, password, logger)

    def send_notification(self, message):
        self.notification.send_notification(message)

    def upload_image(self, path, description):
        # upload instagram bot
        self.insta.upload_post(path, description)

        # upload notification channels
        self.notification.send_notification(description, path)

    def upload_story(self, path):
        self.insta.upload_post(path)