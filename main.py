import sys
from PySide6.QtWidgets import *

from node_editor_window import NodeEditorWindow

def main():    
    #TODO: Better node input
    #TODO: Context menu when right click with extra submenu
    #TODO: Equation from other branch of science

    app = QApplication(sys.argv)
    
    window = NodeEditorWindow()

    app.exec()

if __name__ == '__main__':
    main()
