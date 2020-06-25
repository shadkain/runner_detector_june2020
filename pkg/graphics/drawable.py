from abc import ABCMeta, abstractmethod
from .all import Frame


class Drawable(object):
    __metaclass__ = ABCMeta

    def __init__(self, isHidden=False):
        self.isHidden = isHidden

    @abstractmethod
    def draw(self, frame: Frame):
        '''Draws object providing frame.'''
