

def fibonacci(n, this_dict=None):
    if this_dict is None:
        this_dict = {}
    if n in this_dict:
        return this_dict[n]
    else:
        if n <= 2:
            return 1
        else:
            this_dict[n] = fibonacci(n - 1, this_dict) + fibonacci(n - 2, this_dict)
            return this_dict[n]


print(fibonacci(1000))
print(fibonacci(50))
print(fibonacci(8))
