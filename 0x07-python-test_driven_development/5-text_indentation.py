#!/usr/bin/python3
"""
text_indentation - a function that prints a text with 2 new lines after each of
these characters: ., ? and :
Returns characters printed
"""


def text_indentation(text):
    """
    @text = must be a string, otherwise raise a TypeError exception with the
    message text must be a string
    """
    if isinstance(text, (str)) is False or text is None:
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
