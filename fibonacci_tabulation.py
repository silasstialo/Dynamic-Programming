#A program that uses tabulation technique to calculate the nth fibonacci number
def fibonacci(number):
    table = [0] * (number + 1)
    table[1] = 1
    start = 0
    while start < number:
        table[start + 1] = table[start + 1] + table[start]
        if start + 2 <= number:
            table[start + 2] = table[start + 2] + table[start]
        start += 1

    return table[number]


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(50))
