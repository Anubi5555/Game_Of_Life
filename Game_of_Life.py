class Celija:
    def __init__(self):
        self._status = 'Dead'
    def set_death(self):
        self._status = 'Dead'
    def set_alive(self):
        self._status = 'Alive'
    def is_alive(self):
        if self._status == 'Alive':
            return True
        else:
            return False

    def get_print_character(self):
        if self.is_alive():
            return 'D'
        return 'N'

from cell import Cell
from random import randint

class Board:
    def __init__(self, vrste, kolone):
        self._vrste = vrste 
        self._kolone = kolone