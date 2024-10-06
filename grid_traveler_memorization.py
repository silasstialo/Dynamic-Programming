def grid_traveler(dimension, memo=None):
    if memo is None:
        memo = {}
    if dimension in memo:
        return memo[dimension]
    else:
        if dimension[0] == 0 or dimension[1] == 0:
            return 0
        elif dimension[0] == dimension[1] == 1:
            return 1
        else:
            memo[dimension] = (grid_traveler((dimension[0] - 1, dimension[1]), memo) +
                               grid_traveler((dimension[0], dimension[1] - 1), memo))
            return memo[dimension]


print(grid_traveler((1, 3)))
print(grid_traveler((2, 3)))
print(grid_traveler((3, 3)))
print(grid_traveler((18, 18)))
