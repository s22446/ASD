def head(word):
    return list(word)[0]


def tail(word):
    return word[1:]


def is_empty(word):
    return word == ""


def reverse(word):
    if (is_empty(word) == False):
        reverse(tail(word))
        print(head(word))

# def reverse(word, reversed_word):
#     if (is_empty(word)):
#         return ''.join(reversed_word)
#     else:
#         reversed_word.insert(0, head(word))
#         word = tail(word)
#
#         return reverse(word, reversed_word)
