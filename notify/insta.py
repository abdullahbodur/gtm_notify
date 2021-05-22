from instabot import Bot


class Insta:
    def __init__(self, username: str, password: str, logger):
        # creating an instance bot api
        self.bot = Bot()
        self.bot.login(username=username, password=password)
        self.logger = logger

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
            self.logger.info(f"File Not Found {path} ")

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
            self.logger.info(f"File Not Found {path} ")