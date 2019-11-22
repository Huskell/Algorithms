import numpy as np

def matrix_pow(m, n):

    if m == 0:
        list = [[1, 0], [0, 1]]
        list = np.array(list)
        return list #добавить матрицу в нулевой степени #TODO доделать
    elif m % 2 == 0:
        return matrix_pow(m * m, n/2)
    else:
        return matrix_pow(m, n - 1) * m


