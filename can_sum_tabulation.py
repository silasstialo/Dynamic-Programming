# A program that uses tabulation to efficiently compute wether or nor a target sum can be achieved by adding numbers in an array
def can_sum(number, array):
    table = [False] * (number + 1)
    # it is always possible to generate a target sum of 0: just take no element from the list
    table[0] = True
    current = 0
    while current <= number:
        if table[current] is True:
            for element in array:
                if current + element <= number:
                    table[current + element] = table[current]

        current += 1

    return table[number]


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(300, [7, 14]))
