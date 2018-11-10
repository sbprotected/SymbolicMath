# SymbolicMath
Symbolic math implementation with python

I am going to create a set of classes with python that handle symbolic math.
Here are the plans for my project.

The pastebin page for this project is here: https://pastebin.com/u/sbprotected
Please help me out if you can! I am busy most of the time with schoolwork and other things. Any contributions are welcome and appreciated, so please create a pull request and help out if you can. I will work on this project as much as possible, but it is just a hobby and I cannot dedicate as much time to it as I would like to.

Classes
1. Number
	- This class implements a simple number object

2. Symbol
	- This class implements an object for variables in an expression, such as x, y, or z.

3. Term
	- This class represents a single mathematical term. It is composed of two parts:
		> Coefficient. This is the coefficient on the term, and will be of type Number.
		> Other components. This includes variables (with their exponents) and functions that are part of the term
	- Should implement __(r)add__, __(r)sub__, __(r)mul__, and __(r)truediv__.
 
4. Expression
	- This class represents a series of Term objects, separated by addition or subtraction

5. [Removed]

6. Parser
	- This is one of the primary classes of the project. It should parse a given string into an expression or equation, check for 	errors, and clean up the input.
	- input cleaning such as removing spaces and lowercasing everything
	- error testing should be done and include: parentheses checking, function use.
	- should be able to identify numbers, variables, functions and terms within the input string.
	- should handle implicit multiplication. examples:
		> xx should be parsed to x*x
		> x(x) should be parsed to x*(x)
		> (x)(x) should be parsed to (x)*(x)
		> xsin(x) should be parsed to x*sin(x) but NOT x*s*i*n*(x)
 
7. ExpressionHandler
	- This class handles simple handling of math expressions.
	- simplifying expressions
	- factoring
	- combining like terms: x + x -> 2x, x*x = x^2, etc.

8. Evaluator
	- This class evaluates mathematical expressions for given values of variables.
	- example: evaluate("x^2 - 5x + 6", {"x": 3}) should output 0 because (3)^2 - 5(3) + 6 = 0.

9. EquationSolver
	- This class will implement simple equation solving in a single variable.
	- should be able to solve linear equations using reverse PEMDAS
	- should be able to solve quadratic equations using the quadratic formula, factoring, and completing the square
	- should be able to solve cubic equations using factoring, grouping, and cardano's method.
	- should be able to solve higher degree equations using the Rational Root theorem, synthetic division, descarte's law of 	signs, and the complex conjugate pair root rule
	- when all else fails, it should implement newton's method for approximating zeros.

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
