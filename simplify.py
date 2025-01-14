from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define the equation
equation = (2*x**2 - 3*x + 3)*(x - 1) - (2*x + 1)*(x**2 - 3*x + 2)

# Solve the equation
solution = solve(Eq(equation, 0), x)

# Print the solution
print(f"The solution is: {solution}")