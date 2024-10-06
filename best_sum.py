# A program that uses brute force to compute the best way you can generate the target sum by adding numbers in a provided array
def best_sum(target, array):
    shortest = None
    if target == 0:
        return []
    if target < 0:
        return None
    for number in array:
        remainder = target - number
        result = best_sum(remainder, array)
        if result is not None:
            result = result + [number]
            if shortest is None or len(result) < len(shortest):
                shortest = result

    return shortest


print(best_sum(7, [2, 3]))
print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(7, [2, 4]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(300, [7, 14]))
print(best_sum(100, [1, 2, 5, 25]))
