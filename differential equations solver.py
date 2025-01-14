from sympy import symbols, Function, Eq, dsolve

# Define the variables and the function
x = symbols('x')             # Independent variable
y = Function('y')(x)         # Dependent variable (y is a function of x)

# Define the differential equation
# y*dx + x*(2*x*y + 1)*dy = 0 rewritten as:
# dy/dx = -y / (x * (2*x*y + 1))
deqn = Eq(y.diff(x), -y / (x * (2*x*y + 1)))

# Solve the differential equation
solution = dsolve(deqn, y)

# Output the solution
print("Solution:")
print(solution)