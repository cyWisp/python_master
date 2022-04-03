#!/usr/bin/env python

if __name__ == '__main__':

    user_input = (input("Word: ")).upper()

    vowels = ['A', 'E', 'I', 'O', 'U']
    word_without_vowels = ""

    for letter in user_input:
        for v in vowels:
            if v == letter:
                vowel = True
                break
            else:
                vowel = False
        if vowel is True:
            continue
        else:
            word_without_vowels += letter

    print(word_without_vowels)
