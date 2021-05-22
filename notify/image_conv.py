from PIL import Image, ImageFont, ImageDraw
from .config.asset_conf import AssetConfig as C
from datetime import  datetime


class ImageConv:
    def __init__(self) -> None:
        pass

    def _draw(self, texts: list, image: str, out_image: str, font, color: str):
        """
        it writes given text on image and saves edited image.

        @params :
            - texts (list) : text will written
            - image (str) : no written image
            - out_image (str) : written image
            - font (Font) : custom font
            - color (str) : font color

        @return :
            - None
        """

        with Image.open(C.IMAGE_PATH + image + ".png") as img:

            draw = ImageDraw.Draw(img)

            for t in texts:
                text = t["text"]
                p = t["position"]

                draw.text(p, text, color, font)

            img.save(C.OUT_PATH + out_image + ".png")

    def generate_trading_image(self, trades: list):
        """
        it generates images by using trades list.

        @params :
            - trades (list) : a list includes Trade file

        @return :
            - None
        """

        y = 320

        font = ImageFont.truetype(
            C.FONT_PATH + C.DEFAULT_FONT, C.M_FONT_SIZE, encoding="unic"
        )

        texts = []

        grid = 1080 / 4

        pi = 0

        date = datetime.date(datetime.now())

        for trade in trades:

            texts.append({"position": None, "text": trade["coin"]["name"]})
            texts.append({"position": None, "text": str(trade["buy_price"])})
            texts.append({"position": None, "text": str(trade["sell_price"])})
            texts.append({"position": None, "text": str(trade["profit"]) + "%"})

            size = len(texts)

            for i in range(4):

                w, h = font.getsize(texts[i]["text"])

                x = grid * i + (grid - w) / 2

                texts[size - 4 + i]["position"] = (x, y)

            y += 60

            if y >= 900:
                self._draw(texts, "daily", f"{date}_{pi}", font, C.WHITE)

                y = 320
                texts = []
                pi += 1

        if len(texts) > 0:
            self._draw(texts, "daily", f"{date}_{pi}", font, C.WHITE)
