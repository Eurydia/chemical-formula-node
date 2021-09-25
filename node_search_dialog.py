import sys

from PySide6.QtWidgets import *

from formula import ALL_FORMULAS

class QCuListWidgetItem(QListWidgetItem):
    def __init__(self, class_name):

        self.class_name = class_name
        self.title, tags_searchable, tags_hidden = class_name.search_signature()
        
        self.tags = []
        self.tags.extend(tags_searchable)
        
        text = f'{self.title} ({", ".join(self.tags)})'
        
        self.tags.extend(tags_hidden)

        super().__init__(text)

class QCuDialog(QDialog):
    def __init__(self, grScene=None):
        super().__init__()

        self.grScene = grScene
        
        self.initUI()
    
    def initUI(self):
        self.setFixedSize(250, 600)
        self.layout = QVBoxLayout() 
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.listWidget = QListWidget()
        self.listWidget.itemDoubleClicked.connect(self.add_to_scene)
        for formula in ALL_FORMULAS:
            item = QCuListWidgetItem(formula)
            self.listWidget.addItem(item)
        self.layout.addWidget(self.listWidget)
        
        line = QLineEdit()
        line.textChanged.connect(self.update_filter)
        self.layout.addWidget(line)
        
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Cancel
            )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

        self.setWindowTitle("HELLO!")

    def list_items(self):
        return [self.listWidget.item(row) for row in range(self.listWidget.count())]

    def update_filter(self, text: str):
        hide = []
        text = text.strip()
        if text.startswith('$'):
            text = text.removeprefix('$')
            
            if not text: 
                self.update_list(hide)
                return

            variables = [var.strip() for var in text.split(',')]
            for i, item in enumerate(self.list_items()):
                if not any(var in item.tags for var in variables):
                    hide.append(i)
        else:
            text = text.lower()
            for i, item in enumerate(self.list_items()):
                if not item.text().lower().startswith(text):
                    hide.append(i)
        
        self.update_list(hide)

    def update_list(self, hide):
        for i in range(self.listWidget.count()):
            if i in hide: 
                self.listWidget.item(i).setHidden(True)
            else:
                self.listWidget.item(i).setHidden(False)

    def add_to_scene(self, item: QCuListWidgetItem):
        item.class_name(self.grScene)
        self.accept()

    def accept(self):
        super().accept()
