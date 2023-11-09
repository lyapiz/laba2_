def sum_rows(matrix):
    row_sums = []

    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)

    return row_sums

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_rows(matrix)

for i, row_sum in enumerate(result, 1):
    print(f"Сумма элементов строки {i}: {row_sum}")