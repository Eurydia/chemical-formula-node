from PySide6.QtWidgets import *
from PySide6.QtGui import *

from node_scene import Scene
from node_graphics_view import QCuGraphicsView

class NodeEditorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.initUI()
    
    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        
        self.scene = Scene()

        self.view = QCuGraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor Window")
        self.show()

    # def addDebugContent(self, grScene):
    #     greenBrush = QBrush(Qt.blue)
    #     outlinePen = QPen(QColor('#E4EAF6'))
    #     outlinePen.setWidth(2)

    #     rect = grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
    #     rect.setFlag(QGraphicsItem.ItemIsMovable)

    #     text = grScene.addText("This is my Awesome text!", QFont("Ubuntu"))
    #     text.setFlag(QGraphicsItem.ItemIsSelectable)
    #     text.setFlag(QGraphicsItem.ItemIsMovable)
    #     text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))


    #     widget1 = QPushButton("Hello World")
    #     proxy1 = grScene.addWidget(widget1)
    #     proxy1.setFlag(QGraphicsItem.ItemIsMovable)
    #     proxy1.setPos(0, 30)


    #     widget2 = QTextEdit()
    #     proxy2 = grScene.addWidget(widget2)
    #     proxy2.setFlag(QGraphicsItem.ItemIsSelectable)
    #     proxy2.setPos(0, 60)


    #     line = grScene.addLine(-200, -200, 400, -100, outlinePen)
    #     line.setFlag(QGraphicsItem.ItemIsMovable)
    #     line.setFlag(QGraphicsItem.ItemIsSelectable)

