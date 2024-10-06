# A program that calculates the number of ways you can travel through a 2D grid , starting from the top left corner and ending at the bottom right corner
def grid_traveller(dimension):
    if dimension[0] == 0 or dimension[1] == 0:
        return 0
    elif dimension[0] == dimension[1] == 1:
        return 1
    else:
        return (grid_traveller((dimension[0] - 1, dimension[1])) +
                grid_traveller((dimension[0], dimension[1] - 1)))


print(grid_traveller((1, 3)))
print(grid_traveller((2, 3)))
print(grid_traveller((3, 3)))
print(grid_traveller((18, 18)))
