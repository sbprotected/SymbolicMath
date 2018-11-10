from string import ascii_lowercase;


class Symbol():

    """ Represents a mathematical symbol in an expression such as x, y, or z """

    def __init__(self, symbol="x"):
        if symbol in ascii_lowercase:
            self.symbol = symbol;
        else:
            raise ValueError("Symbol must be a lowercase letter.");

    def __repr__(self):
        return "Symbol( {} )".format(self.symbol);
