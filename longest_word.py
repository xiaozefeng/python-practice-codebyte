# coding: utf-8

__author__ = 'steven'

def longest_word(sen):

    # first web remove non alphanumeric character from the string
    # using the translate function which deletes the specified characters
    # sen = sen.translate(None, "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")
    map = str.maketrans("~!@#$%^&*()-_+={}[]:;'<>?/,.|`", "")
    sen = sen.translate(map)

    # now we separate the string into alist of words
    arr = sen.split(' ')

    # the list max function will return the element in arr
    # with the longest length because web specify key=len
    return max(arr, key=len)

print('the longest wrod : %s' % longest_word('the $$$longest# word is coderbyte'))
