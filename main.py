def interpol1(x, y, x_val, n):
    for i in range(n):
        if x_val >= x[i] and x_val <= x[i + 1]:
            return (y[i] + (y[i + 1] - y[i]) * (x_val - x[i]) / (x[i + 1] - x[i]))


def newton_interpolation(x, y):
    """
    Вычисляет интерполяционный многочлен в форме Ньютона.

    :param x: Список узлов интерполяции (x-координаты).
    :param y: Список соответствующих значения функции в узлах интерполяции.
    :return: Интерполяционный многочлен в форме Ньютона.
    """
    n = len(x)
    if n != len(y):
        raise ValueError("Списки x и y должны иметь одинаковую длину")

    # Создаем таблицу разделенных разностей
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])

    # Строим многочлен в форме Ньютона
    def newton_poly(x_val):
        result = f[0][0]
        x_term = 1
        for i in range(1, n):
            x_term *= (x_val - x[i - 1])
            result += f[0][i] * x_term
        return result

    return newton_poly

# Пример использования

x = []
y = []
n = int(input())
for i in range(n):
    args = [float(i) for i in input().split()]
    x.append(args[0])
    y.append(args[1])

interpolation_poly = newton_interpolation(x, y)
x_val = float(input())
result1 = interpol1(x, y, x_val, n)

# Вычисление значения многочлена в точке
result2 = interpolation_poly(x_val)
print(f'А)Значение интерполяционного многочлена в точке {x_val} равно {result1}')
print(f'Б)Значение интерполяционного многочлена в точке {x_val} равно {result2}')
