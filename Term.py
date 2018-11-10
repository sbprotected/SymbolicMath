from Number import Number;
from Symbol import Symbol;


# this is what I am currently working on. I have to figure out how to implement
# addition and division operations with terms that may or may not have the same variables and degree.
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

    def __neg__(self):
        return self * Term(Number(-1), [], []);

    def __add__(self, other):
        if self.syms + self.exps == other.syms + other.exps:
            return Term(self.coef + other.coef, self.syms, self.exps);
        else:
            # not sure what to put here. if this block executes it means
            # that the two terms do not have the same exponents and degrees and cannot be combined.
            raise NotImplementedError;

    def __sub__(self, other):
        return self + -other;

    def __mul__(self, other):
        f = dict(zip(map(lambda v: v.symbol, self.syms), self.exps));
        for var, exp in zip(other.syms, other.exps):
            var = var.symbol;
            if var in f.keys():
                f[var] += exp;
            else:
                f[var] = exp;
        return Term(self.coef * other.coef, list(map(lambda e: Symbol(e), f.keys())), list(f.values()))

    def __truediv__(self, other):
        f = dict(zip(map(lambda v: v.symbol, self.syms), self.exps));
        new_numerator, new_denominator = {}, {};

        for var, exp in zip(other.syms, other.exps):
            var = var.symbol;
            if var in f.keys():
                f[var] -= exp;
                number = f[var];
            else:
                f[var] = -exp;

            null = Number(0);

            if number < null:
                new_denominator[var] = -number;
            elif number > null:
                new_numerator[var] = number;
            else:
                pass; # if the new exponent is 0, don't include it.

        new_coef = self.coef / other.coef;

        numerator_term = Term(Number(new_coef.numerator),
                              list(map(lambda v: Symbol(v), new_numerator.keys())),
                              list(new_numerator.values()));
        denominator_term = Term(Number(new_coef.denominator),
                                list(map(lambda v: Symbol(v), new_denominator.keys())),
                                list(new_denominator.values()));

        if denominator_term == Term(Number(1), [], []):
            return numerator_term;
        else:
            # not sure what to do here either. if this block executes it means
            # that the division could not be simplified to a single term...
            raise NotImplementedError;

    def __eq__(self, other):
        return (self.coef, self.syms, self.exps) == (other.coef, other.syms, other.exps);
