from pint import Unit, Quantity
from sympy import Symbol, solvers
from PySide6.QtWidgets import *

from node_content_widget import QCuNodeContentWidget
from node_graphics_node import QCuGraphicsNode

class FormulaNode:
    def __init__(
        self, 
        grScene,
        width,
        variables, 
        title='FORMULA NAME'):
        
        self.grScene = grScene
        self.title = title
        self.width = width
        self.variables = variables

        self.var_calc = []

        self.content = QCuNodeContentWidget(self)
        self.grNode = QCuGraphicsNode(self)
        self.grScene.addItem(self.grNode)  
    
    def update_value(self):
        input_entered = sum(1 for lineEdit, _ in self.content.input_fields if lineEdit.text())
        if input_entered != len(self.variables) - 1:
            self.content.outputLabel.setText('')
            return

        self.var_calc = []
        base_unit, calc_unit = self.prepare_variables()
        equality = self.create_equation()
        self.solve_equation(equality, calc_unit, base_unit)

    def prepare_variables(self):
        base_unit = None
        calc_unit = None
        for variable, key in zip(self.content.input_fields, self.variables.keys()):
            lineEdit, comboBox = variable
            var = lineEdit.text()
            unit_name = comboBox.currentText()
            if var:
                try:
                    quantified = Quantity(float(var), unit_name)
                except ValueError:
                    pass
                quantified_base_unit = quantified.to(self.variables[key])
                magnitude = quantified_base_unit._magnitude
            else:
                magnitude = Symbol(key)
                base_unit = self.variables[key]
                calc_unit = Unit(unit_name)
            self.var_calc.append(magnitude)

        return base_unit, calc_unit

    def create_equation(self):
        pass

    def solve_equation(self, equation, base_unit, calc_unit):
        magnitude = solvers.solve_linear(equation)[1]
        quantity = Quantity(magnitude, base_unit).to(calc_unit)

        self.content.outputLabel.setText(str(quantity))

    def remove(self):
        self.grScene.removeItem(self.grNode)
        self.grNode.node = None
        self.grNode = None
        self.content.node = None
        self.content = None
    
    @classmethod
    def search_signature(cls):
        pass
