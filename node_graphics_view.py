from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from node_search_dialog import QCuDialog

class QCuGraphicsView(QGraphicsView):
    def __init__(self, grScene, parent=None):
        super().__init__(parent)
    
        self.grScene = grScene
        
        self.initUI()
        
        self.setScene(self.grScene)

        self.zoomClamp = True
        self.zoomInFactor = 1.25
        self.zoom = 5
        self.zoomStep = 1
        self.zoomRange =[0, 10]
    
    def initUI(self):
        self.setRenderHints(
            QPainter.Antialiasing | 
            QPainter.TextAntialiasing | 
            QPainter.SmoothPixmapTransform)
        
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPress(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonPress(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonPress(event)
        else: 
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(event)
        elif event.button() == Qt.RightButton:
            self.rightMouseButtonRelease(event)
        elif event.button() == Qt.LeftButton:
            self.leftMouseButtonRelease(event)
        else: 
            super().mouseReleaseEvent(event)
    
    def middleMouseButtonPress(self, event: QMouseEvent):
        releaseEvent = QMouseEvent(
            QEvent.MouseButtonRelease, 
            event.localPos(),
            event.screenPos(),
            Qt.LeftButton, 
            Qt.NoButton,
            event.modifiers()
        )
        super().mouseReleaseEvent(releaseEvent)

        self.setDragMode(QGraphicsView.ScrollHandDrag)

        fakePressEvent = QMouseEvent(
            event.type(),
            event.localPos(),
            event.screenPos(),
            Qt.LeftButton, 
            event.buttons() | Qt.LeftButton,
            event.modifiers()
        )
        super().mousePressEvent(fakePressEvent)

    def middleMouseButtonRelease(self, event: QMouseEvent):
        fakeReleaseEvent = QMouseEvent(
            event.type(),
            event.localPos(),
            event.screenPos(),
            Qt.LeftButton,
            event.buttons() & ~Qt.LeftButton,
            event.modifiers()
        )
        super().mouseReleaseEvent(fakeReleaseEvent)

        self.setDragMode(QGraphicsView.NoDrag)

    def leftMouseButtonPress(self, event: QMouseEvent):
        if event.modifiers() == Qt.ShiftModifier:
            event.ignore()
            fakeEvent = QMouseEvent(
                QEvent.MouseButtonPress, 
                event.localPos(), 
                event.screenPos(),
                Qt.LeftButton, 
                event.buttons() | Qt.LeftButton,
                event.modifiers() | Qt.ControlModifier
                )
            super().mousePressEvent(fakeEvent)
            return

        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self, event: QMouseEvent):
        if event.modifiers() == Qt.ShiftModifier:
            event.ignore()
            fakeEvent = QMouseEvent(
                event.type(), 
                event.localPos(),
                event.screenPos(),
                Qt.LeftButton, 
                Qt.NoButton,
                event.modifiers() | Qt.ControlModifier
                )
            super().mouseReleaseEvent(fakeEvent)
            return

        return super().mouseReleaseEvent(event)
    
    def rightMouseButtonPress(self, event: QMouseEvent):
        return super().mousePressEvent(event)
    
    def rightMouseButtonRelease(self, event: QMouseEvent):
        return super().mouseReleaseEvent(event)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() != Qt.ControlModifier:
            return 

        zoomOutFactor = 1 / self.zoomInFactor

        if event.angleDelta().y() > 0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep 
        else: 
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep
        
        clamped = False
        if self.zoom < self.zoomRange[0]: self.zoom, clamped = self.zoomRange[0], True
        if self.zoom > self.zoomRange[1]: self.zoom, clamped = self.zoomRange[1], True

        if not clamped or not self.zoomClamp:
            self.scale(zoomFactor, zoomFactor)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Delete:
            self.delete_selected()
            return

        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Space:
            self.create_search_window()
            return

        return super().keyPressEvent(event)
    
    def create_search_window(self):
        dialog = QCuDialog(self.grScene)
        dialog.exec()

    def delete_selected(self):
        for item in self.grScene.selectedItems():
            item.node.remove()

    def getItemAtClick(self, event):
        pos = event.pos()
        obj = self.itemAt(pos)
        return obj

