from Number import Number;
from Symbol import Symbol;


# this is what I am currently working on. I have to figure out how to implement
# the basic arithmetic operations with terms that may or may not have the same variables and degree.
# example: x + x = 2x, x^2 + x = x^2 + x (cannot be simplified: different degree), x + y = x + y (cannot be simplified: different variable)


class Term():

    """ Represents a single mathematical term such as 2xy or 3x^2 """

    def __init__(self, coefficient, symbols, exponents):
        self.coef = coefficient;
        if len(symbols) == len(exponents):
            self.syms, self.exps = symbols, exponents;
        else:
            raise ValueError("There must be an equal number of symbols and exponents");

    def __repr__(self):
        return "Term( {}{} )".format(self.coef.as_decimal(), "".join(("{}^{}".format(sym.symbol, exp.as_decimal()) for sym, exp in zip(self.syms, self.exps))));

    def __add__(self, other):
        pass;

    def __sub__(self, other):
        pass;

    def __mul__(self, other):
        pass;

    def __truediv__(self, other):
        pass;
