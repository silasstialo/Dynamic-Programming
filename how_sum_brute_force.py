# A program that uses brute force to calculate how you can gegerate a target sum by adding numbers in the array of numbers
def how_sum(target, array):
    if target == 0:
        return []
    if target < 0:
        return None
    else:
        for number in array:
            remainder = target - number
            result = how_sum(remainder, array)
            if result is not None:
                result.append(number)
                return result
        return None


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
