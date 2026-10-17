def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here

	m = len(matrix)
	n = len(matrix[0])

	b = [[0 for col in range(n)] for row in range(m)]

	for row in range(m):
		for col in range(n):
			b[row][col] = matrix[row][col] * scalar

	return b
