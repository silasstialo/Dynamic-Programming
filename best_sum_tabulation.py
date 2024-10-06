# A program that uses tabulation to compute the best way to generate the target sum by adding numbers in the numbers array
def best_sum(number, array):
    table = [None] * (number + 1)
    table[0] = []
    current = 0
    while current <= number:
        if table[current] is not None:
            for element in array:
                if element + current <= number:
                    current_combo = table[current] + [element]
                    if table[current + element] is None or len(current_combo) < len(table[current + element]):
                        table[current + element] = current_combo
        current += 1
    return table[number]


print(best_sum(7, [2, 3]))
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(7, [2, 4]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(300, [7, 14]))
print(best_sum(100, [1, 2, 5, 25]))
