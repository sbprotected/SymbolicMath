from math import gcd;


def nth_root(n, index):
    return n ** (1 / index);


class Number():

    """ Object for representing numerical values in an expression """

    def __init__(self, value=0):
        if isinstance(value, (int, float)):
            self.numerator, self.denominator = float(value).as_integer_ratio();
        elif isinstance(value, tuple):
            if len(value) == 2 and value[1] != 0:
                self.numerator, self.denominator = map(int, value);
            else:
                raise ValueError("tuple must be of length 2 and the denominator cannot be 0.");
        else:
            raise TypeError("value must be a float, int, or 2-tuple of ints.");
        self.reduce();

    def __repr__(self):
        return "Number( {} / {} )".format(self.numerator, self.denominator);

    def __neg__(self):
        return Number(-1) * self;

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

    def __pow__(self, other):
        return Number((nth_root(self.numerator, other.denominator) ** other.numerator,
                      nth_root(self.denominator, other.denominator) ** other.numerator));

    def __eq__(self, other):
        return (self.numerator, self.denominator) == (other.numerator, other.denominator);

    def __lt__(self, other):
        return self.as_decimal()  < other.as_decimal();

    def __gt__(self, other):
        return self.as_decimal() > other.as_decimal();

    def as_decimal(self):
        """ return the value in decimal form. """
        return self.numerator / self.denominator;

    def reduce(self):
        """ Simplify the fraction """
        common_divisor = gcd(self.numerator, self.denominator);
        self.numerator //= common_divisor;
        self.denominator //= common_divisor;
