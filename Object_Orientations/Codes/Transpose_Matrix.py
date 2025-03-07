def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6]]

print(transpose(matrix1))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(transpose(matrix2))  # Output: [[1, 4], [2, 5], [3, 6]]
