from pint import Unit
from sympy import Equality

from node_node import FormulaNode

class IdealGasLaw(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'P': Unit('torr'),
            'V': Unit('liter'),
            'n': Unit('mol'),
            'T': Unit('kelvin')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Ideal Gas Law')       

    def create_equation(self):
        print(self.var_calc)
        P, V, n, T = self.var_calc
        R = 62.363577
        return Equality(P*V, n*R*T)

    @classmethod
    def search_signature(cls):
        return 'Ideal Gas Law', ('P', 'V', 'n', 'R', 'T'), tuple()


class CharlesLaw(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'V1': Unit('liter'),
            'T1': Unit('kelvin'),
            'V2': Unit('liter'),
            'T2': Unit('kelvin')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Charles\' Law')

    def create_equation(self):
        print(self.var_calc)
        V1, T1, V2, T2 = self.var_calc
        return Equality(V1/T1, V2/T2)

    @classmethod
    def search_signature(cls):
        return 'Charles\' Law', ('V1', 'T1', 'V2', 'T2'), ('V', 'T')


class BoylesLaw(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'P1': Unit('pascal'),
            'V1': Unit('liter'),
            'P2': Unit('pascal'),
            'V2': Unit('liter')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Boyle\'s Law')

    def create_equation(self):
        print(self.var_calc)
        P1, V1, P2, V2 = self.var_calc
        return Equality(P1*V1, P2*V2)

    @classmethod
    def search_signature(cls):
        return 'Boyle\'s Law', ('P1', 'V1', 'P2', 'V2'), ('V', 'P')


class GayLussacsLaw(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'P1': Unit('pascal'),
            'T1': Unit('kelvin'),
            'P2': Unit('pascal'),
            'T2': Unit('kelvin')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Gay-Lussac\'s Law')

    def create_equation(self):
        print(self.var_calc)
        P1, T1, P2, T2 = self.var_calc
        return Equality(P1/T1, P2/T2)

    @classmethod
    def search_signature(cls):
        return 'Gay-Lussac\'s Law', ('P1', 'T1', 'P2', 'T2'), ('T', 'P')


class CombinedGasLaw(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'P1': Unit('pascal'),
            'V1': Unit('liter'),
            'T1': Unit('kelvin'),
            'P2': Unit('pascal'),
            'V2': Unit('liter'),
            'T2': Unit('kelvin')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Combined Gas Law')

    def create_equation(self):
        print(self.var_calc)
        P1, V1, T1, P2, V2, T2 = self.var_calc
        return Equality((P1*V1)/T1, (P2*V2)/T2)

    @classmethod
    def search_signature(cls):
        return 'Combined Gas Law', ('P1', 'V1' 'T1', 'P2', 'V2', 'T2'), ('T', 'P', 'V')


class Molality(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'n': Unit('mol'),
            'g': Unit('kilogram'),
            'm': Unit('mol') / Unit('kg')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Molality')

    def create_equation(self):
        n, g, m = self.var_calc
        return Equality(n/g, m)

    @classmethod
    def search_signature(cls):
        return 'Molality', ('n', 'g', 'm'), tuple()


class Molarity(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'n': Unit('mol'),
            'V': Unit('liter'),
            'M': Unit('mol') / Unit('liter')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Molarity')

    def create_equation(self):
        n, V, M = self.var_calc
        return Equality(n/V, M)

    @classmethod
    def search_signature(cls):
        return 'Molarity', ('n', 'V', 'M'), tuple()


class MolarMass(FormulaNode):
    
    def __init__(self, grScene):
        variables = {
            'n': Unit('mol'),
            'g': Unit('gram'),
            'MW': Unit('gram') / Unit('mol')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Molar Mass')

    def create_equation(self):
        n, g, MM = self.var_calc
        return Equality(g/n, MM)

    @classmethod
    def search_signature(cls):
        return 'Molar Mass', ('n', 'g', 'MW'), tuple()


class VolumeSTP(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'V': Unit('liter'),
            'T': Unit('kelvin'),
            'P': Unit('torr'),
            'Vstp': Unit('liter')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Volume STP')

    def create_equation(self):
        V, T, P, Vstp = self.var_calc
        return Equality(Vstp,V*(273.15/T)*(P/760))

    @classmethod
    def search_signature(cls):
        return 'Volume STP', ('V', 'T', 'P', 'Vstp'), tuple('STP')


class MolSTP(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'nstp': Unit('mol'),
            'Vstp': Unit('liter')
            }
        width = 150

        super().__init__(grScene, width, variables, 'Mol STP')

    def create_equation(self):
        nstp, Vstp = self.var_calc
        return Equality(nstp, Vstp/22.4)

    @classmethod
    def search_signature(cls):
        return 'Mol STP', ('n', 'Vstp', 'nstp'), tuple('STP')


class Dilution(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'M1': Unit('mol')/Unit('liter'),
            'V1': Unit('mol'),
            'M2': Unit('mol')/Unit('liter'),
            'V2': Unit('mol'),
            }
        width = 150

        super().__init__(grScene, width, variables, 'Dilution')

    def create_equation(self):
        M1, V1, M2, V2 = self.var_calc
        return Equality(M1*V1, M2*V2)

    @classmethod
    def search_signature(cls):
        return 'Dilution', ('M1', 'V1', 'M2', 'V2'), tuple('V', 'M')


class PercentConcentrationWByV(FormulaNode):
    def __init__(self, grScene):
        variables = {
            'M1': Unit('mol')/Unit('liter'),
            'V1': Unit('mol'),
            'M2': Unit('mol')/Unit('liter'),
            'V2': Unit('mol'),
            }
        width = 150

        super().__init__(grScene, width, variables, 'Dilution')

    def create_equation(self):
        M1, V1, M2, V2 = self.var_calc
        return Equality(M1*V1, M2*V2)

    @classmethod
    def search_signature(cls):
        return 'Dilution', ('M1', 'V1', 'M2', 'V2'), tuple('V', 'M')

        
ALL_FORMULAS = (
    IdealGasLaw, CharlesLaw, BoylesLaw, GayLussacsLaw,  Molality, Molarity, MolarMass,
    VolumeSTP, MolSTP, Dilution)
