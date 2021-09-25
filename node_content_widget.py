from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class QCuNodeContentWidget(QWidget):
    def __init__(self, node, parent=None):
        super().__init__(parent)

        self.node = node
        self.variables = node.variables
        
        self.input_fields =  []
        
        self.initUI()
    
    def initUI(self):
        self.layout = QGridLayout()
        self.layout.setContentsMargins(10, 0, 10, 0)
        self.setLayout(self.layout)

        for row, key in enumerate(self.variables.keys()):
            variableInputLabel = QLabel(key)
            self.layout.addWidget(variableInputLabel, row, 0)

            lineEditInput = QLineEdit()
            lineEditInput.setPlaceholderText(f'enter value for {key}')
            lineEditInput.setValidator(QDoubleValidator())
            lineEditInput.setClearButtonEnabled(True)
            lineEditInput.textChanged.connect(self.update_value)
            self.layout.addWidget(lineEditInput, row, 1)

            comboboxInput = QComboBox()
            units = []
            try:
                extra_units = sorted(str(u) for u in self.variables[key].compatible_units())
                units.extend(extra_units)
            except KeyError:
                units.append(str(self.variables[key]))

            for unit in units:
                comboboxInput.addItem(unit)

            comboboxInput.currentIndexChanged.connect(self.update_value)
            self.layout.addWidget(comboboxInput, row, 2, 1, 2)

            self.input_fields.append((lineEditInput, comboboxInput))
    
        lblout = QLabel('RESULT')
        self.layout.addWidget(lblout, len(self.variables), 0)

        self.outputLabel = QLabel()
        self.layout.addWidget(self.outputLabel, len(self.variables), 1, 1 ,2)

    def update_value(self):
        self.node.update_value()
