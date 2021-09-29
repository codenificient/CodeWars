def disemvowel(string_):
    myvowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U', 'I']

    for letter in string_:
        if letter in myvowels:
            string_ = string_.replace(letter, '')
    return string_