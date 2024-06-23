from pyspark import SparkContext, SparkConf
from pyspark.mllib.linalg.distributed import CoordinateMatrix, MatrixEntry

# Создание контекста Spark
conf = SparkConf().setAppName("SparseMatrixMultiplication").setMaster("local")
sc = SparkContext(conf=conf)

# Пример разреженных матриц
# Матрица A (3x2)
entries_a = [
    MatrixEntry(0, 0, 1.0), MatrixEntry(0, 1, 2.0),
    MatrixEntry(1, 0, 3.0), MatrixEntry(1, 1, 4.0),
    MatrixEntry(2, 0, 5.0), MatrixEntry(2, 1, 6.0)
]

# Матрица B (2x4)
entries_b = [
    MatrixEntry(0, 0, 7.0), MatrixEntry(0, 1, 8.0), MatrixEntry(0, 2, 9.0), MatrixEntry(0, 3, 10.0),
    MatrixEntry(1, 0, 11.0), MatrixEntry(1, 1, 12.0), MatrixEntry(1, 2, 13.0), MatrixEntry(1, 3, 14.0)
]

# Создание разреженных матриц
matrix_a = CoordinateMatrix(sc.parallelize(entries_a))
matrix_b = CoordinateMatrix(sc.parallelize(entries_b))

# Умножение матриц
result = matrix_a.toBlockMatrix().multiply(matrix_b.toBlockMatrix())

# Преобразование результата обратно в CoordinateMatrix для получения результатов
result_coord = result.toCoordinateMatrix()

# Сборка и печать результатов
result_entries = result_coord.entries.collect()
for entry in result_entries:
    print(f"({entry.i}, {entry.j}) -> {entry.value}")

# Остановка контекста Spark
sc.stop()

