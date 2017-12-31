from genetic.element import Element
from typing import List


class Population(object):
    def __init__(self, size: int=100):
        self.elements: List[Element] = [Element() for _ in range(size)]
        self.size: int = size

    def update(self):
        for element in self.elements:
            element.update()