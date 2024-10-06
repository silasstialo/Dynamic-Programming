# A program that computes the number of ways the target word can be constructed by concatenating the strings in the wordbank array
def count_construct(target_word, wordbank):
    way_counter = 0
    if target_word == "":
        return 1
    for word in wordbank:
        if target_word.startswith(word):
            new_word = target_word[len(word):]
            total_ways_new_word = count_construct(new_word, wordbank)
            way_counter = way_counter + total_ways_new_word

    return way_counter


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
