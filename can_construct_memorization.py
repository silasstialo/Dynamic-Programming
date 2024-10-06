def can_construct(target_word, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target_word in memo:
        return memo[target_word]
    if target_word == "":
        return True
    for word in wordbank:
        if target_word.startswith(word):
            new_word = target_word[len(word):]
            if can_construct(new_word, wordbank, memo):
                memo[target_word] = True
                return True

    memo[target_word] = False
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
