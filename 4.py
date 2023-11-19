import numpy as np

a = np.array([0, 0, 1, 2, 0, 3, 0, 3, 4, 2])
kk = np.array(np.where([a == 0])[1])
kk +=1
print(max(kk))
