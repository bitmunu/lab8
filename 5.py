import numpy as np
from scipy.stats import multivariate_normal
import time


def density(X, m, C):
    D = len(m)
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    norm_factor = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)

    diff = X - m
    exponent = -0.5 * np.sum(diff @ inv_C * diff, axis=1)

    log_density_vals = norm_factor + exponent
    return log_density_vals

np.random.seed(42)
N = 1000
D = 3
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = C @ C.T

start = time.time()
result_custom = density(X, m, C)
custom_dur = time.time() - start

start= time.time()
result_scipy = multivariate_normal(m, C).logpdf(X)
scipy_dur = time.time() - start

print(f"самостоятельная реализация: {result_custom} \n время: {custom_dur}")
print(f"через scipy.stats.multivariate_normal: {result_scipy} \n время: {scipy_dur}")

