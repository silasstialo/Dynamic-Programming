def count_construct(target_word, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target_word in memo:
        return memo[target_word]
    way_counter = 0
    if target_word == "":
        return 1
    for word in wordbank:
        if target_word.startswith(word):
            new_word = target_word[len(word):]
            total_ways_new_word = count_construct(new_word, wordbank, memo)
            way_counter = way_counter + total_ways_new_word

    memo[target_word] = way_counter
    return way_counter


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
