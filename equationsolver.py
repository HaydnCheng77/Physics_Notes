import sympy as sp

# Define symbols
m, M, u, theta, phi = sp.symbols('m M u theta phi')
v1, V = sp.symbols('v1 V')

# Conservation equations
momentum_x = sp.Eq(m*u, m*v1*sp.cos(theta) + M*V*sp.cos(phi))
momentum_y = sp.Eq(0, m*v1*sp.sin(theta) - M*V*sp.sin(phi))
energy = sp.Eq(m*u**2, m*v1**2 + M*V**2)

# Solve for V in terms of v1 and phi (from y-momentum)
V_expr = sp.solve(momentum_y, V)[0]
print("V in terms of v1:", V_expr)

# Substitute V into the energy equation
energy_sub = energy.subs(V, V_expr)
v1_squared = sp.solve(energy_sub, v1**2)[0]
print("v1^2:", v1_squared)

# Substitute V and v1^2 into x-momentum
momentum_x_sub = momentum_x.subs([(V, V_expr), (v1**2, v1_squared)])
momentum_x_sub = sp.simplify(momentum_x_sub)
print("Momentum x-component simplified:", momentum_x_sub)

# Define tan(theta) explicitly
tan_theta = sp.tan(theta)
tan_phi = sp.tan(phi)

# Solve for tan(theta)
try:
    tan_theta_expr = sp.simplify(sp.solve(momentum_x_sub, tan_theta)[0])
    print("tan(theta):", tan_theta_expr)
except IndexError:
    print("Error: Could not solve for tan(theta).")