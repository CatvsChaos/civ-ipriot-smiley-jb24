import time
from blinkable import Blinkable
from smiley import Smiley


class Sad(Smiley, Blinkable):

    def __init__(self):
        """
        Instantiates a Smiley with a sad expression.
        """
        # [3.4.1]
        super().__init__(complexion = self.BLUE)

        self.draw_mouth()
        self.draw_eyes()

    """    
        # [3.1]
        self.colour_face()

    # [3.1]
    def colour_face(self):
    
        # Changes face colour on a smiley
        
        face = [0,1,2,3,4,5,6,7,
                8,9,10,11,12,13,14,15,
                16,17,18,19,20,21,22,23,
                24,25,26,27,28,29,30,31,
                32,33,34,35,36,37,38,39,
                40,41,42,43,44,45,46,47,
                48,49,50,51,52,53,54,55,
                56,57,58,59,60,61,62,63]

        for pixel in face:
            if pixel not in [0, 7, 56, 63,
                            49, 54, 42, 43, 44, 45,
                            10, 13, 18, 21]:
                # [3.2] OOP: Abstraction & Encapsulation
                self.pixels[pixel] = self.complexion()
    """

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley.
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley.
        :param wide_open: Render eyes wide open or shut.
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                #eyes = self.GREEN
                # [3.2]
                eyes = self.complexion()
            self.pixels[pixel] = eyes

    def blink(self, delay=.30):
        """
        Blinks the smiley's eyes once.
        :param delay: Delay between blinks (in seconds).
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()