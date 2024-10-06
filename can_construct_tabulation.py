#A program that uses tabulation to efficientlt tabulate whether or not a targtet word can be constructed by concatenating strings in a word bank
def can_construct(word, wordbank):
    table = [False] * (len(word) + 1)
    table[0] = True
    current = 0
    while current < len(table):
        if table[current] is True:
            for string in wordbank:
                if word[current:].startswith(string):
                    if current + len(string) <= len(table):
                        table[current + len(string)] = table[current]
        current += 1

    return table[-1]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
