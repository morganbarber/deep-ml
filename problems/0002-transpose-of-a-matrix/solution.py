def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    n = len(a)
    m = len(a[0])

    b = [[0 for col in range(n)] for row in range(m)]

    for row in range(n):
        for col in range(m):
            b[col-1][row-1]=a[row-1][col-1]

    return b