import cv2
from abc import ABCMeta, abstractproperty
from .all import Frame, Drawable
from pkg.errors import Error


class Window(object):
    '''Abstract window class.'''
    __metaclass__ = ABCMeta

    def __init__(self, name: str):
        self.name = name
        self.__children = []

    def addChild(self, child: Drawable):
        '''Adds drawable child in drawing queue. Children will be drawn on every call of window.draw'''
        if not isinstance(child, Drawable):
            raise Error('Cannot add nondrawable child')

        self.__children.append(child)

    @abstractproperty
    def frame(self) -> Frame:
        '''Frame that provides drawing operations.'''

    def draw(self):
        for child in self.__children:
            if not child.isHidden:
                child.draw(self.frame)

    def show(self):
        cv2.imshow(self.name, self.frame.data)
        cv2.waitKey(1)

    def waitKey(self):
        cv2.waitKey()