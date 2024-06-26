# ode/ode.py

"""
Este Módulo calcula los valores de la solución de la ecuación diferencial dada
usando 3 distintos métodos, Euler, Runge-Kutta 2 y Runge-Kutta 4

Además genera 3 gráficas para comparar la precisión de cada método.
"""

import numpy as np
import matplotlib.pyplot as plt
import os


# Ecuación Diferencial
def f(x, y):
    """
    Función que define la ecuación diferencial.

    Argumentos:
    x -- valor de la variable independiente
    y -- valor de la variable dependiente

    Retorna:
    Valor de la derivada en el punto (x, y).
    """
    return 0.1 * np.sqrt(y) + 0.4 * x ** 2


# Método de Euler
def fEuler(x, y, xf, n):
    """
    Resuelve la ecuación diferencial usando el método de Euler.

    Argumentos:
    x  -- valor inicial de la variable independiente
    y  -- valor inicial de la variable dependiente
    xf -- valor final de la variable independiente
    n  -- número de pasos

    Genera:
    Gráfica con la función resuelta usando el método de Euler

    Retorna:
    Arrays de valores de x e y.
    """

    y0 = y
    x0 = x
    h = (xf - x0) / n
    # Inicialización de arrays
    x = np.linspace(x0, xf, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y


# Método Runge-Kutta 2
def fRK2(x, y, xf, n):
    """
    Resuelve la ecuación diferencial usando el método de Runge-Kutta 2.

    Argumentos:
    x  -- valor inicial de la variable independiente
    y  -- valor inicial de la variable dependiente
    xf -- valor final de la variable independiente
    n  -- número de pasos

    Genera:
    Gráfica con la función resuelta usando el método de Runge-Kutta 2

    Retorna:
    Arrays de valores de x e y.
    """

    y0 = y
    x0 = x
    h = (xf - x0) / n
    # Inicialización de arrays
    x = np.linspace(x0, xf, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        y[i + 1] = y[i] + k2
    return x, y


# Método Runge-Kutta 4
def fRK4(x, y, xf, n):
    """
    Resuelve la ecuación diferencial usando el método de Runge-Kutta 4.

    Argumentos:
    x  -- valor inicial de la variable independiente
    y  -- valor inicial de la variable dependiente
    xf -- valor final de la variable independiente
    n  -- número de pasos

    Genera:
    Gráfica con la función resuelta usando el método de Runge-Kutta 4

    Retorna:
    Arrays de valores de x e y.
    """

    y0 = y
    x0 = x
    h = (xf - x0) / n
    # Inicialización de arrays
    x = np.linspace(x0, xf, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return x, y


def plot_and_save(method, x0, y0, xf, n, filename, title):
    x, y = method(x0, y0, xf, n)
    plt.figure()
    plt.plot(x, y, label=title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend()
    plt.grid(True)

    # Utilizar os.makedirs para crear directorios si no existen
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    plt.savefig(filename)
    plt.close()


# Parámetros comunes
x0 = 2
y0 = 4
xf = 5
n = 20

# Ejemplos de llamadas a plot_and_save con los métodos deseados
plot_and_save(fEuler, x0, y0, xf, n, './docs/graficas/Euler.png', 'Método de Euler')
plot_and_save(fRK2, x0, y0, xf, n, './docs/graficas/RungeKutta2.png', 'Método de Runge-Kutta 2')
plot_and_save(fRK4, x0, y0, xf, n, './docs/graficas/RungeKutta4.png', 'Método de Runge-Kutta 4')