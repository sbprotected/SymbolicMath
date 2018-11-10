from math import gcd;


class Number():

    """ Object for representing numerical values in an expression """

    def __init__(self, value=0):
        if isinstance(value, (int, float)):
            self.numerator, self.denominator = float(value).as_integer_ratio();
        elif isinstance(value, tuple):
            if len(value) == 2 and value[1] != 0:
                self.numerator, self.denominator = value;
            else:
                raise ValueError("tuple must be of length 2 and the denominator cannot be 0.");
        else:
            raise TypeError("value must be a float, int, or 2-tuple of ints.");
        self.reduce();

    def __repr__(self):
        return "Number( {} / {} )".format(self.numerator, self.denominator);

    def __add__(self, other):
        numerator = self.numerator + other.numerator;
        denominator = gcd(self.denominator, other.denominator);
        return Number((numerator, denominator));

    def __sub__(self, other):
        numerator = self.numerator - other.numerator;
        denominator = gcd(self.denominator, other.denominator);
        return Number((numerator, denominator));

    def __mul__(self, other):
        numerator = self.numerator * other.numerator;
        denominator = self.denominator * other.denominator;
        return Number((numerator, denominator));

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator;
        denominator = self.denominator * other.numerator;
        return Number((numerator, denominator));

    def as_decimal(self):
        """ return the value in decimal form. """
        return self.numerator / self.denominator;

    def reduce(self):
        """ Simplify the fraction """
        common_divisor = gcd(self.numerator, self.denominator);
        self.numerator /= common_divisor;
        self.denominator /= common_divisor;
