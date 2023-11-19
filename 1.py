import numpy as np

with open('1_input.txt', 'r') as file:
    lines = file.readlines()

data = []
for line in lines:
    row = [int(num) for num in line.strip().split(',')]
    data.append(row)

matrix = np.array(data)
total_sum = np.sum(matrix)

max_element = np.max(matrix)
min_element = np.min(matrix)

print(f"Сумма всех элементов: {total_sum}")
print(f"Максимальный элемент: {max_element}")
print(f"Минимальный элемент: {min_element}")
