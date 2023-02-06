
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment

def christofides(points):
    n = points.shape[0]
    d = squareform(pdist(points))
    r = np.arange(n)
    d = np.column_stack([r, d])
    m = np.min(d[d[:, 1] > 0, 1])
    C = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if d[i, j] <= m:
                C[i, j] = C[j, i] = 1
    odd_vertices = [v for v in range(n) if sum(C[v, :]) % 2 != 0]
    T = np.zeros((n, n))
    for s in odd_vertices:
        D = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if C[i, j] == 1:
                    D[i, j] = d[i, j]
        row_ind, col_ind = linear_sum_assignment(D)
        for i, j in zip(row_ind, col_ind):
            T[i, j] = T[j, i] = 1
            C[i, j] = C[j, i] = 0
    Euler = [0]
    for i in range(1, n):
        for j in range(i):
            if T[i, j] == 1:
                Euler.extend([i, j])
                break
    path = [Euler[0]]
    for i in range(1, len(Euler)):
        for j in range(i + 1, len(Euler)):
            if Euler[j] == path[-1]:
                path.append(Euler[i])
                break
    return path

points = np.random.rand(1000, 2)
path = christofides(points)
