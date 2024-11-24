from sense_hat import SenseHat


class Smiley:
    """
    Provides a Smiley template with default expression.
    """
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    # [3.3.1]
    def __init__(self, complexion = YELLOW):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()

        #Y = self.YELLOW

        # [3.3.2]
        self.my_complexion = complexion

        # [3.3.3]
        X = self.my_complexion

        O = self.BLANK

        # [3.3.3]
        self.pixels = [
            O,X,X,X,X,X,X,O,
            X,X,X,X,X,X,X,X,
            X,X,X,X,X,X,X,X,
            X,X,X,X,X,X,X,X,
            X,X,X,X,X,X,X,X,
            X,X,X,X,X,X,X,X,
            X,X,X,X,X,X,X,X,
            O,X,X,X,X,X,X,O]

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)

    # [3.2]
    def complexion(self):
        """
        Control smiley face colour.
        """
        # [3.2]
        #return self.complexion
        # [3.3.3]
        return self.my_complexion
