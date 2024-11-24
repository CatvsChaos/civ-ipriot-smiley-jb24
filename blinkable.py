from abc import ABC, abstractmethod


class Blinkable(ABC):
    """
    Specify what anything that claims to be 'blinkable' should be able to do.
    Check if the subclass has implemented the blink method below.
    """
    @abstractmethod
    def blink(self):
        pass
