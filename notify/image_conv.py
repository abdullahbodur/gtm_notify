import traceback
from PIL import Image, ImageFont, ImageDraw
from .config.asset_conf import AssetConfig as C
from datetime import datetime


from .data import Data

class ImageConv:
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
            rgb_im = img.convert("RGB")
            rgb_im.save(C.OUT_PATH + out_image + ".jpg")

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

        images = []

        for _id in trades:

            try:
                trade = trades[_id]
                texts.append({"position": None, "text": trade.coin})
                texts.append({"position": None, "text": str(trade.buy_price)})
                texts.append({"position": None, "text": str(trade.sell_price)})
                texts.append(
                    {"position": None, "text": self._handle_profit(trade.profit)}
                )

                size = len(texts)

                for i in range(4):

                    w, h = font.getsize(texts[i]["text"])

                    x = grid * i + (grid - w) / 2

                    texts[size - 4 + i]["position"] = (x, y)

                y += 60

                if y >= 900:
                    img_name = f"{date}_{pi}"

                    images.append(C.OUT_PATH + img_name + ".jpg")

                    self._draw(texts, "daily", img_name, font, C.WHITE)

                    y = 320
                    texts = []
                    pi += 1
            except Exception:
                exc = traceback.format_exc()
                Data.logger.error(exc)
                continue

        if len(texts) > 0:

            img_name = f"{date}_{pi}"

            images.append(C.OUT_PATH + img_name + ".jpg")
            self._draw(texts, "daily", img_name, font, C.WHITE)

        return images

    def _handle_profit(self, profit):

        profit = "{:.2f}%".format(profit)

        return profit if "-" in profit else ("+" + profit)
