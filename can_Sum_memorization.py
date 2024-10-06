def can_sum(target, array, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    else:
        if target == 0:
            return True
        if target < 0:
            return False
        for n in array:
            remainder = target - n
            if can_sum(remainder, array, memo):
                memo[target] = True
                return True
        memo[target] = False
        return False


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(300, [7, 14]))
