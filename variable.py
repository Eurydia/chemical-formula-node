from abc import ABC, abstractmethod
from enum import Enum, auto
from sympy import *
from pint import Quantity


class VariableType(Enum):
    PRESSURE = auto()
    VOLUME = auto()
    MASS = auto()
    MOLE = auto()
    TEMPERATURE = auto()

class Formula:
    def __init__(self):
        pass

    def solve(self):
        pass
