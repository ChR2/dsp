# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        return "Number of donuts: %d" %(count)
    else:
        return "Number of donuts: many"


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) > 2:
        y = s[:2] + s[-2:]
        return y
    else:
        return ' '



def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    first_char = s[0]
    new_word = [s[0]]

    for i in s[1:]:
        if i == first_char:
            new_word.append('*')
        else:
            new_word.append(i)
    new_string = ''.join(new_word)
    return new_string


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """

    a1 = a[:2]
    a2 = a[2:]
    b1 = b[:2]
    b2 = b[2:]
    word = b1 + a2 + ' '+ a1 +b2
    return word


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s) > 3:
        if s[-3:] == 'ing':
            new_word = s + 'ly'
        else:
            new_word = s[:-3] + 'ing'
        return new_word
    else:
        return s


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    snot = s.find("not")
    sbad = s.find("bad")

    if sbad > snot:
        s = s.replace(s[snot:(sbad+3)], 'good')
    return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    a_len = len(a)
    b_len = len(b)

    if a_len % 2 == 0:
        a_index = a_len // 2
    else:
        a_index = (a_len // 2) + 1

    if b_len % 2 == 0:
        b_index = b_len // 2
    else:
        b_index = (b_len // 2) + 1

    a_front = a[0:a_index]
    a_back = a[a_index:]

    b_front = b[0:b_index]
    b_back = b[b_index:]

    return a_front + b_front + a_back + b_back

print(donuts(4))
print(donuts(9))
print(donuts(10))
print(donuts(99))

print(both_ends('spring')) #'spng'
print(both_ends('Hello')) #'Helo'
print(both_ends('a')) #''
print(both_ends('xyz')) #'xyyz'

print(fix_start('babble'))#'ba**le'
print(fix_start('aardvark'))#'a*rdv*rk'
print(fix_start('google'))#'goo*le'
print(fix_start('donut'))#'donut'

print(mix_up('mix', 'pod'))#'pox mid'
print(mix_up('dog', 'dinner'))#'dig donner'
print(mix_up('gnash', 'sport'))#'spash gnort'
print(mix_up('pezzy', 'firm'))#'fizzy perm'

print(verbing('hail'))#'hailing'
print(verbing('swiming'))#'swimingly'
print(verbing('do'))#'do'

print(not_bad('This movie is not so bad'))#'This movie is good'
print(not_bad('This dinner is not that bad!'))#'This dinner is good!'
print(not_bad('This tea is not hot'))#'This tea is not hot'
print(not_bad("It's bad yet not"))#"It's bad yet not"

print(front_back('abcd', 'xy'))#'abxcdy'
print(front_back('abcde', 'xyz'))#'abcxydez'
print(front_back('Kitten', 'Donut'))#'KitDontenut'

