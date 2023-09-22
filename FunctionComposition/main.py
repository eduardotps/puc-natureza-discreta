from sympy import symbols, lambdify
import re

x = symbols('x')

def insert_multiplication(s):
    return re.sub(r'(\d)([a-zA-Z])', r'\1*\2', s)

def compose(f_str, g_str, value):
    f = lambdify(x, f_str)
    g = lambdify(x, g_str)

    return g(f(value)), f(g(value))

if __name__ == "__main__":
    f_str = insert_multiplication(input("Digite a função f(x) (ex: x^2): ").replace('^', '**'))
    g_str = insert_multiplication(input("Digite a função g(x) (ex: x-1): ").replace('^', '**'))

    value = int(input("Digite o valor de x: "))

    g_f, f_g = compose(f_str, g_str, value)

    print(f"(g ° f)({value}) = {g_f}")
    print(f"(f ° g)({value}) = {f_g}")
