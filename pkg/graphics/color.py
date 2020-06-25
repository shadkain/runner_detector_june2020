class Color(object):
    @staticmethod
    def black():
        return Color(0, 0, 0)
 
    @staticmethod
    def white():
        return Color(255, 255, 255)

    @staticmethod
    def red():
        return Color(255, 0, 0)

    @staticmethod
    def green():
        return Color(0, 255, 0)

    @staticmethod
    def blue():
        return Color(0, 0, 255)

    @staticmethod
    def yellow():
        return Color(255, 255, 0)

    @staticmethod
    def magenta():
        return Color(255, 0, 255)

    @staticmethod
    def cyan():
        return Color(0, 255, 255)

    def __init__(self, r: int, g: int, b: int):
        self.r = r; self.g = g; self.b = b

    @property
    def bgr(self) -> (int, int, int):
        '''Returns BGR color model tuple.'''
        return self.b, self.g, self.r