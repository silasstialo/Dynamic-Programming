#A program that takes an integer and an array of integer as arguments and determines if you can achieve the target sum by adding number in the array

def can_Sum(target, array):
    if target == 0:
        return True
    if target < 0:
        return False
    for n in array:
        remainder = target - n
        if can_Sum(remainder, array) is True:
            return True
    return False
    
    
print(can_Sum(7, [2, 3]))
print(can_Sum(7, [5, 3, 4, 7]))
print(can_Sum(7, [2, 4]))
print(can_Sum(300, [7, 14]))
