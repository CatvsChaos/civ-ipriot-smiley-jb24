import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    """
    Provides a Smiley with an angry expression.
    """
    def __init__(self):
        # [3.4.1]
        super().__init__(complexion = self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws furrowed brow and open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        brow = [17,18,19,20,21,22]
        for pixel in brow:
            self.pixels[pixel] = self.BLANK

        eyes = [26,29]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                # [3.2]
                eyes = self.complexion()
            self.pixels[pixel] = eyes


    def blink(self, delay=.30):
        """
        Blinks the smiley's eyes once.
        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()