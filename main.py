import numpy as np


def cramer_solve(A, b):
    n = A.shape[0]
    det_A = np.linalg.det(A)

    if np.isclose(det_A, 0):
        raise ValueError("Система несовместна или имеет бесконечно много "
                         "решений (det(A) = 0)")

    x = np.zeros(n, dtype=complex)

    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        det_Ai = np.linalg.det(Ai)
        x[i] = det_Ai / det_A

    return x


n = int(input("Введите размерность системы n: "))
print("Введите матрицу A построчно (через пробел):")
A = np.array([list(map(complex, input().split())) for _ in range(n)], dtype=complex)
print("Введите вектор b (через пробел):")
b = np.array(list(map(complex, input().split())), dtype=complex)

try:
    solution = cramer_solve(A, b)
    print("Решение системы:", solution)
except ValueError as e:
    print("Ошибка:", e)
