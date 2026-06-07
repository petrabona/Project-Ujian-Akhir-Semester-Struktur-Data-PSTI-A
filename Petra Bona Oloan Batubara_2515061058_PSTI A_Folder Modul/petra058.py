def add_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2 or not matrix1[0] or not matrix2[0]:
        raise ValueError("Matriks tidak boleh kosong.")
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Matriks harus memiliki dimensi yang sama untuk penjumlahan.")
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result
def invert_matrix(matrix):
    n = len(matrix)
    if n == 0 or not matrix[0]:
        raise ValueError("Matriks tidak boleh kosong.")
    if n != len(matrix[0]):
        raise ValueError("Matriks harus persegi untuk diinversi.")
    if n == 2:
        a, b = matrix[0][0], matrix[0][1]
        c, d = matrix[1][0], matrix[1][1]
        determinant = a * d - b * c
        if determinant == 0:
            raise ValueError("Matriks adalah singular dan tidak dapat diinversi.")
        inv_det = 1.0 / determinant
        return [
            [d * inv_det, -b * inv_det],
            [-c * inv_det, a * inv_det]
        ]
    elif n == 3:
        det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
               matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
               matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
        if det == 0:
            raise ValueError("Matriks adalah singular dan tidak dapat diinversi.")
        inv_det = 1.0 / det
        adj = [
            [
                (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]),
                -(matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1]),
                (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1])
            ],
            [
                -(matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]),
                (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]),
                -(matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0])
            ],
            [
                (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]),
                -(matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0]),
                (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
            ]
        ]
        inverted = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(adj[j][i] * inv_det)
            inverted.append(row)
        return inverted
    else:
        raise ValueError("Inversi hanya didukung untuk matriks 2x2 dan 3x3 tanpa pustaka eksternal.")
def create_identity_matrix(size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Ukuran harus merupakan bilangan bulat positif.")
    identity = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1.0)
            else:
                row.append(0.0)
        identity.append(row)
    return identity
def multiply_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2 or not matrix1[0] or not matrix2[0]:
        raise ValueError("Matriks tidak boleh kosong.")
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    if cols1 != rows2:
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua untuk perkalian.")
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result