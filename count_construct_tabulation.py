# A program that uses tabulation to compute the totaal number of ways a target string can be constructes using by concatenating strings in the  wordbank array
def count_construct(word, wordbank):
    table = [0] * (len(word) + 1)
    table[0] = 1
    # it is always possible to create an empty string: by taking no words from wordbank
    current = 0
    while current < len(table):
        if table[current] != 0:
            for string in wordbank:
                if word[current:].startswith(string):
                    if current + len(string) <= len(table):
                        table[current + len(string)] += table[current]

        current += 1

    return table[-1]


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
