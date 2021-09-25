from node_graphics_scene import QCuGraphicsScene

from PySide6.QtWidgets import *

class Scene:
    def __init__(self):
        self.nodes = []
        
        self.scene_wdith = 64000
        self.scene_height = 64000

        self.initUI()
    
    def initUI(self):
        self.grScene = QCuGraphicsScene(self)
        self.grScene.setGrScene(self.scene_wdith, self.scene_height)

