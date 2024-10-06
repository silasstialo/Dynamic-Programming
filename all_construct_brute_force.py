# A program that accepts a target word and an array of strings. it returns a 2d array containing all of the ways the target can be constructed by concatenating elements of the wordbank array.
def all_construct(target_word, wordbank):
    ways = []
    if target_word == "":
        return [[]]
    for word in wordbank:
        if target_word.startswith(word):
            new_word = target_word[len(word):]
            ways_new_word = all_construct(new_word, wordbank)
            [x.insert(0, word) for x in ways_new_word]
            ways.extend(ways_new_word)

    return ways


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
