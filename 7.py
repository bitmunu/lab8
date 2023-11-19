import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species_column = iris[:, -1]
unique, species_count = np.unique(species_column, return_counts=True)

print("значения: ", unique)
print("количество вхождений: ", species_count)