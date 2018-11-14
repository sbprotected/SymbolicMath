import re, json;
from string import ascii_lowercase;

digit = re.compile(r"\d");
operators = "+-*/^";

with open("functions.json", "r") as file:
    functions = json.load(file);


class Token():

    def __init__(self, type_, value):
        self.type = type_;
        self.value = value;

    def __repr__(self):
        return "{}( '{}' )".format(self.type, self.value);


def tokenize(string):
    tokens, variable_buffer, number_buffer = [], "", "";
    string = string.replace(" ", "");

    def push_variable_tokens():
        nonlocal variable_buffer;
        length = len(variable_buffer);
        for i in range(length):
            tokens.append(Token("variable", variable_buffer[i]));
            if i < length - 1: tokens.append(Token("operator", "*"));
        variable_buffer = "";

    def push_number_token():
        nonlocal number_buffer;
        if number_buffer:
            tokens.append(Token("number", number_buffer));
            number_buffer = "";

    for char in string:
        if digit.match(char) or char == ".":
            number_buffer += char;
        elif char in ascii_lowercase:
            if number_buffer:
                push_number_token();
                tokens.append(Token("operator", "*"));
            variable_buffer += char;
        elif char in operators:
            push_number_token();
            push_variable_tokens();
            tokens.append(Token("operator", char));
        elif char == "(":
            if variable_buffer:
                if variable_buffer in functions:
                    tokens.append(Token("function", variable_buffer));
                    variable_buffer = "";
                else:
                    push_variable_buffer();
                    tokens.append(Token("operator", "*"));
            elif number_buffer:
                push_number_token();
                tokens.append(Token("operator", "*"));
            tokens.append(Token("left parenthesis", char));
        elif char == ")":
            push_variable_tokens();
            push_number_token();
            tokens.append(Token("right parenthesis", char));
        elif char == ",":
            push_number_token();
            push_variable_tokens();
            tokens.append(Token("argument separator", char));

    push_number_token();
    if variable_buffer: push_variable_tokens();

    return tokens;

def get_tokens(string):
    yield from tokenize(string);
