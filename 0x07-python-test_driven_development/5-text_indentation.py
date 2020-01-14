#!/usr/bin/python3
"""
print_square - a function that prints a text with 2 new lines after each of
these characters: ., ? and :
Returns a text
"""


def text_indentation(text):
    """
    @text = must be a string, otherwise raise a TypeError exception with the
    message text must be a string
    """
    if isinstance(text, (str)) is None or text is False:
        raise TypeError("text must be a string")
    flag = False
    _text = text.strip()
    pattern = set(".?:")
    for i in _text:
        if i == " " and flag is True:
            print("", end="")
            flag = False
        else:
            print(i, end="")
        if any(j in i for j in pattern):
            print ("", end="\n\n")
            flag = True
