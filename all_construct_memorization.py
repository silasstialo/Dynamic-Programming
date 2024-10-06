def all_construct(target_word, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target_word in memo:
        return memo[target_word]
    ways = []
    if target_word == "":
        return [[]]
    for word in wordbank:
        if target_word.startswith(word):
            new_word = target_word[len(word):]
            ways_new_word = all_construct(new_word, wordbank, memo)
            [x.insert(0, word) for x in ways_new_word]
            ways.extend(ways_new_word)

    memo[target_word] = ways
    return ways


print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))