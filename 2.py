import numpy as np

def encode(x):
    ff = np.array(np.where([x[:-1] != x[1:]])[1])
    rer = (np.r_[0, ff + 1, len(x)])
    return(x[rer[:-1]], np.diff(rer))


a = np.array([1, 1, 1, 2, 2, 3, 3, 3, 4, 2])
print(encode(a))
