import queue
import threading
from os import path
from .config.config import Config as C
import apprise


class NotificationHandler:
    def __init__(self, enabled=True):
        
        if enabled and path.exists(C.APPRISE_CONFIG_PATH):
            self.app = apprise.Apprise()
            config = apprise.AppriseConfig()
            config.add(C.APPRISE_CONFIG_PATH)
            self.app.add(config)
            self.queue = queue.Queue()
            self.start_worker()
            self.enabled = True

        else:
            self.enabled = False

    def start_worker(self):

        threading.Thread(target=self.process_queue, daemon=True).start()

    def process_queue(self):
        """
        This function push message to bot if any body receive to its.
        First it gets body and attachments (if already sended) from queue.
        After that, it notifies

        @params
            -None

        @return
            -None

        """
        while True:  # for always run.
            message, attachments = self.queue.get()

            if attachments:
                self.app.notify(body=message, attach=attachments)
            else:
                self.app.notify(body=message)
            self.queue.task_done()

    def send_notification(self, message, attachments=None):
        """
        This function queues the given message to send.

        @params
            -None

        @return
            -None

        """

        if self.enabled:
            self.queue.put((message, attachments or []))