def derivative(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m / step_size

def my_function(x):
    return x**2
slope_at_2 = derivative(my_function, 2, 0.0001)

print(slope_at_2)