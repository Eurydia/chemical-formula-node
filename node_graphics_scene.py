from math import ceil, floor

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class QCuGraphicsScene(QGraphicsScene):
    def __init__(
        self, 
        scene,
        parent=None):
        super().__init__(parent)

        self.scene = scene
        
        self.gridSqure = 5
        self.gridSize = 50

        self._color_background = QColor("#405CB1")
        self._color_light = QColor("#E4EAF6")

        self.pen_light = QPen(self._color_light)
        self.pen_light.setWidth(1)
        self.pen_heavy = QPen(self._color_light)
        self.pen_heavy.setWidth(4)
        self.pen_extra_heavy = QPen(self._color_light)
        self.pen_extra_heavy.setWidth(16)

        self.setBackgroundBrush(self._color_background)

    def setGrScene(self, width, height):
        self.setSceneRect(
            -(width // 2),
            -(height // 2),
            width,
            height)

    def drawBackground(self, painter: QPainter, rect):
        super().drawBackground(painter, rect)
        
        left = int(floor(rect.left()))
        right = int(ceil(rect.right()))
        top = int(floor(rect.top()))
        bottom = int(ceil(rect.bottom()))

        first_left_line = left - (left % self.gridSize)
        first_top_line = top - (top % self.gridSize)

        lines_light, lines_heavy, lines_extra_heavy = [], [], []
        for v in range(first_left_line, right, self.gridSize):
            l = QLine(v, top, v, bottom) 
            if v % (self.gridSize * self.gridSqure * self.gridSqure) == 0: lines_extra_heavy.append(l)
            elif v % (self.gridSize * self.gridSqure) == 0: lines_heavy.append(l)
            else: lines_light.append(l)

        for h in range(first_top_line, bottom, self.gridSize):
            l = QLine(left, h, right, h)
            if h % (self.gridSize * self.gridSqure * self.gridSqure) == 0: lines_extra_heavy.append(l)
            elif h % (self.gridSize * self.gridSqure) == 0: lines_heavy.append(l)
            else: lines_light.append(l)

        painter.setPen(self.pen_light)
        painter.drawLines(lines_light)
        
        painter.setPen(self.pen_heavy)
        painter.drawLines(lines_heavy)

        painter.setPen(self.pen_extra_heavy)
        painter.drawLines(lines_extra_heavy)
