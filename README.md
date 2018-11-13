# SymbolicMath
Symbolic math implementation with python

I am creating a set of classes with python that handle symbolic math.
Here's what's been done so far, in addition to plans for the future.

The pastebin page for this project is here: https://pastebin.com/u/sbprotected
Please help me out if you can! I am busy most of the time with schoolwork and other things. Any contributions are welcome and appreciated, so please create a pull request and help out if you can. I will work on this project as much as possible, but it is just a hobby and I cannot dedicate as much time to it as I would like to.

Classes
1. Number
	- This class implements a simple number object
	- It represents all numbers as integer ratios. This eliminates floating point errors and nothing is lost
	- when dealing with irrational numbers because those can't be fully represented anyway.
	- this class can handle addition, subtraction, multiplication, division, exponentiation, unary negation operator,
	equality testing, and comparison operators <, >. 
	- the class is located in `Number.py` in the repository.

2. Symbol
	- This class implements an object for variables in an expression, such as x, y, or z.
	- it is located in the `Symbol.py` file in the repository.

3. Term
	- This class represents a single mathematical term. It is composed of three parts:
		- Coefficient. This is the coefficient on the term, and is be of type Number.
		- variables of the term, which are stored as Symbol objects in a list.
		- exponents, each which corresponds to one of the variables in the variable list. they are of type Number
	- supports the unary negation operator, arithmetic functions, and comparison operators.
	- for addition, subtraction and division, there is no current implemented way to handle the case where the two operands
	do not combine into a single term after the operation. e.g. x + y cannot be combined, and it remains x + y.
	- the class is located in `Term.py` in the repository.
 
4. Expression
	- If I decide to make this (which seems unlikely at this point, there doesn't really appear to be any need for it), it will
	represent an expression, or sequence of Term objects.

5. [Removed]

6. Parser
	- This is one of the primary classes of the project. It parses a given string into an expression or equation, checks for 	errors, and cleans up the input.
	- input cleaning such as removing spaces and lowercasing everything
	- error testing should be done and include: parentheses checking, function use.
	- able to identify numbers, variables, and terms within the input string.
	- handles implicit multiplication. examples:
		> xx should be parsed to x*x
		> x(x) should be parsed to x*(x)
		> (x)(x) should be parsed to (x)*(x)
		> xsin(x) should be parsed to x*sin(x) but NOT x*s*i*n*(x)
	- functions such as sine and cosine will be implemented in the future, but for now the primary focus is handling simpler terms.
	- the class is located in `Parser.py` in the repository.
		
 
7. ExpressionHandler
	- This class will handle simple handling of math expressions.
	- simplifying expressions
	- factoring
	- combining like terms: x + x -> 2x, x*x = x^2, etc.

8. Evaluator
	- This class will evaluate mathematical expressions for given values of variables.
	- example: evaluate("x^2 - 5x + 6", {"x": 3}) should output 0 because (3)^2 - 5(3) + 6 = 0.

9. EquationSolver
	- This class will implement simple equation solving in a single variable.
	- should be able to solve linear equations using reverse PEMDAS
	- should be able to solve quadratic equations using the quadratic formula, factoring, and completing the square
	- should be able to solve cubic equations using factoring, grouping, and cardano's method.
	- should be able to solve higher degree equations using the Rational Root theorem, synthetic division, descarte's law of 	signs, and the complex conjugate pair root rule
	- when all else fails, it should implement newton-raphson method for approximating zeros.

10. InequalitySolver
	- This class will implement simple inequality solving in a single variable.
	- should implement region testing
	- should be able to handle inequalities with absolute values.

11. Plotter
	- This class will use a graphics library and the Evaluator class to plot points and functions.
	- should be able to estimate derivatives using a difference quotient with a very small delta x value
	- should be able to estimate integrals using a Riemann sum with very small incremental widths

12. MathEngine
	- this class will tie all of the other classes together, in an interactive (text-based) interface.
	- should be able to read input such as plot(function), evaluate(function)
	- should be able to create variables, store their values, and use them
	- should be savable, implemented using pickle.
