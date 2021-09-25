from math import ceil

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class QCuGraphicsNode(QGraphicsItem):
    def __init__(self, node, parent=None):
        super().__init__(parent)
        
        self.node = node

        self._title_color = Qt.white
        self._title_font = QFont("Ubuntu", 13)
        self._title_font.setBold(True)
        
        self.content = self.node.content

        self.title_height = 25 * (ceil(len(node.title) / node.width))
        self.width = self.node.width * 3
        self.height = ((len(self.node.variables) + 1) * 31) + self.title_height
        self.edge_size = 10.0
        self._padding = 10

        self._brush_title = QBrush(QColor('#5B75C4'))
        self._brush_background = QBrush(QColor('#405CB1'))
        self._pen_default = QPen(QColor('#E4EAF6'))
        self._pen_default.setWidth(3)
        self._pen_selected = QPen(QColor('#DDC798'))
        self._pen_selected.setWidth(3)

        self.title = self.node.title
        self.initTitle()

        self.initContent()
 
        self.initUI()

    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)

    def initContent(self):
        self.grContent = QGraphicsProxyWidget(self)
        self.content.setGeometry(
            self.edge_size, 
            self.title_height + self.edge_size, 
            self.width - (2*self.edge_size),
            self.height - self.title_height - (2*self.edge_size)
            )
        self.grContent.setWidget(self.content)
        
    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)
        self.title_item.setPos(self._padding, 0)
        self.title_item.setTextWidth(self.width - (2 * self._padding))
        self.title_item.setPlainText(self.title)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        # Drawing title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(
            0, 
            0, 
            self.width, 
            self.height, 
            self.edge_size, 
            self.edge_size
            )
        path_title.addRect(
            0, 
            self.title_height - self.edge_size, 
            self.edge_size, 
            self.edge_size
            )
        path_title.addRect(
            self.width - self.edge_size, 
            self.title_height - self.edge_size, 
            self.edge_size, 
            self.edge_size
            )
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        #Drawing contents
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(
            0,
            self.title_height, 
            self.width,
            self.height - self.title_height,
            self.edge_size, 
            self.edge_size
            )
        path_content.addRect(0, 
            self.title_height,
            self.edge_size, 
            self.edge_size
            )
        path_content.addRect(
            self.width - self.edge_size,
            self.title_height,
            self.edge_size, 
            self.edge_size
        )
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())

        #Drawing outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(
            0, 
            0, 
            self.width, 
            self.height, 
            self.edge_size, 
            self.edge_size
            )
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

    def boundingRect(self):
        return QRectF(
            0, 0, 
            (2 * self.edge_size) + self.width, 
            (2 * self.edge_size) + self.height
        ).normalized()
