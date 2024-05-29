import sympy as sp
from sympy import expand, factor

x, y, g_x, g_y, g_a, g_b, g_c = sp.symbols('d_x d_y g_x g_y g_a g_b g_c')

x_vec = sp.Matrix([x , y])

g = sp.Matrix([[g_a, g_c], [g_c, g_b]])

F =  x_vec.transpose() @ g @ x_vec
print(F[0])
expr = sp.simplify(factor(F[0]))
print(sp.collect(expr, [x - g_x]))

# a,b = sp.symbols('x_i y_j')

# x_vec_new = sp.Matrix([x - a - g_x, y - b - g_y])

# P = x_vec_new.transpose() @ g @ x_vec_new

# print(P[0])

# c = F[0] - P[0]

# # 化简


# expr = sp.simplify(factor(c))
# expr = sp.simplify((c))
# # 打印化简结果
# print(expr)
# print(sp.collect(expr, [a-x]))

# # print(sp.s)

