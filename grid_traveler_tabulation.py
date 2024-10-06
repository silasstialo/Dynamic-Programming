# A program that uses tabulation to efficiently compute the number of ways you cam move through a 2D list
def grid_travel(rows, columns):
    table = [[0 for i in range(columns + 1)] for j in range(rows + 1)]
    table[1][1] = 1

    for i in range(rows + 1):
        for j in range(columns + 1):
            current = table[i][j]
            if j < columns:
                table[i][j + 1] += current
            if i < rows:
                table[i + 1][j] += current

    return table[rows][columns]


print(grid_travel(1, 1))
print(grid_travel(2, 3))
print(grid_travel(3, 2))
print(grid_travel(10, 3))
print(grid_travel(3, 3))
print(grid_travel(18, 18))
