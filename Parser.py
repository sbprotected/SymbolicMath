import re;
from string import ascii_lowercase;
from Number import Number;
from Symbol import Symbol;
from Term import Term;


number_pattern = re.compile(r"([-]?[0-9]*\.?[0-9]+)");
operators = "+-*/^";
variables = ascii_lowercase;
delimiters = operators + "()";

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ^ b,
};


class Parser():

    """
    Parser for symbolic math expressions.
    There isn't much use of the actual Parser object; all methods are class methods.
    Putting it into a class was more of an organizational decision.
    """

    def get_numbers(self, expr=""):
        """ find and return all occurences of decimal numbers in expr """
        return [match[0] for match in number_pattern.findall(expr)];

    @classmethod
    def separate(cls, string, chars=" "):
        """ separates a string at the specified delimiters (chars) """
        temp, l = "", [];

        for char in string:
            if not char in chars:
                temp += char;
            else:
                if temp: l.append(temp);
                l.append(char);
                temp = "";

        if string and (not string[-1] in chars): l.append(temp);
        return l;

    @classmethod
    def list_index(cls, list_, chars):
        """ equivalent to list.index but with searches for multiple characters at once """
        for i, element in enumerate(list_):
            if element in chars:
                return i;
        return -1;

    @classmethod
    def get_parentheses_location(cls, list_):
        """ Gets the index of the first opening parenthesis and the matching close parenthesis """
        start, count = list_.index("("), 1;
        for i, element in enumerate(list_[start+1:]):
            if element == "(":
                count += 1;
            elif element == ")":
                count -= 1;
            if not count:
                end = i;
                break;
        return start, start+end+1;

    @classmethod
    def list_replace(cls, list_, start, end, replacement):
        """ replaces list[start:end+1] with replacement in a given list. """
        return list_[:start] + [replacement] + list_[end+1:];

    @classmethod
    def clean_up(cls, expr):
        """ remove whitespace, simplify operators, and handle implicit multiplication """
        if expr:
            expr = expr.lower().replace(" ", "").replace("++", "+").replace("--", "+").replace("+-", "-");
            newexpr = expr[0];
            for i, char in enumerate(expr[1:], start=1):
                if ((char in variables+"(") and (expr[i-1] not in operators+"(")):
                    newexpr += "*{}".format(char);
                else:
                    newexpr += char;
            return newexpr;
        else:
            return "";

    @classmethod
    def test_term(cls, term):
        """ test the term for basic errors with parentheses and operators """
        if "+" in term:
            raise SyntaxError("Expressions separated by + are multiple terms.");
        elif term in delimiters:
            return;

        if any([oper in term[0]+term[-1] for oper in "*/^"]):
            raise SyntaxError("Term cannot begin or end with an operator.");

        if ("(" in term) or (")" in term):
            if term.count("(") > term.count(")"):
                raise SyntaxError("There are more opening parentheses than closing ones.");

            # the number of ( must always be the same or lower as the number of )
            for i in range(len(term)):
                substring = term[:i];
                if substring.count("(") < substring.count(")"):
                    raise SyntaxError("Close parenthesis detected, but no parentheses were open");

    @classmethod
    def list_substitute(cls, terms, index):
        """ substitute [operation(a, b)] in a list for [a, operation, b] """
        # example: ["x", * "x"] -> ["x^2"]
        operation = operations[terms[index]];
        result = operation(terms[index-1], terms[index+1]);
        # ^^ it is safe to assume that there will be no IndexError here because
        # Parser.test_term checks for illicit operator placement.
        return terms[:index-1] + [result] + terms[index+2:];

    @classmethod
    def parse_term(cls, term):
        """ Parse a string into a Term object """
        #
        # tests the term for syntactical errors
        # then cleans up the string
        # if it is a compound term like 3x^2 it first expands that to 3*x^2
        # then parses 3 and x^2 separately, then simplifies it to a single term.
        #

        if isinstance(term, Term): return term;

        cls.test_term(term);
        term = cls.clean_up(term);
        terms = cls.separate(term, "*/()");

        while "(" in terms:
            start, end = cls.get_parentheses_location(terms);
            result = cls.parse_term("".join(terms[start+1:end]));
            terms = cls.list_replace(terms, start, end, result);
            
        if len(terms) == 1:
            term = terms[0];
            if number_pattern.fullmatch(term):
                # its a number
                return Term(Number(float(term)), [], []);
            elif term in delimiters:
                # it is an operator or parenthesis
                return term;
            elif "^" in term:
                # it was not a Number, operator, or parenthesis.
                # it is something of the form (var)^(exponent)
                return Term(Number(1), [Symbol(term[0])], [Number(float(term[term.rfind("^")+1:]))]);
            else:
                # it is just a single variable such as "x" or "y"
                return Term(Number(1), [Symbol(term)], [Number(1)]);     
        else:
            # it is not possible for recursion depth to exceed 2 here.
            terms = [cls.parse_term(t) for t in terms];

        while "*" in terms or "/" in terms:
            index = cls.list_index(terms, ["*", "/"]);
            # ^^ this will be the first occurence of an operator.
            terms = cls.list_substitute(terms, index);

        return terms[0];


if __name__ == "__main__":
    parser = Parser();
    term1 = "(8/32x)(4x)";
