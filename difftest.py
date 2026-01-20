# from sympy import *

# x = symbols('x')

# f = x**2
                            # 이 코드는 심파이를 이용한 도함수 계산임
# dx_f = diff(f)
# print(dx_f)       




# 이코드는 파이썬 기본 문법을 이용한 도함수 계산임


# def f(x):
#     return x**2

# def dx_f(x):
#     return 2*x

# slope_at_2 = dx_f(2.0)

# print(slope_at_2)

# from sympy import *
# from sympy.plotting import plot3d

# x,y = symbols('x y')

# f = 2*x**3 + 3*y**3

# f_2 = 2*x**5 + 3*y**5

# dx_f = diff(f, x)
# dy_f = diff(f, y)

# print(dx_f)
# print(dy_f)
# plot3d(f_2)


from sympy import *

x = symbols('x')
z = (x**2 + 1)**3-2
dz_dx = diff(z,x)
print(dz_dx)