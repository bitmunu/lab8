import numpy as np

a = np.random.randn(10, 4)

print(a)
print(f"Max = {a.max()}")
print(f"Min = {a.min()}")
print(f"Mean = {a.mean()}")
print(f"Std = {a.std()}")

b = a[:5]
print(b)