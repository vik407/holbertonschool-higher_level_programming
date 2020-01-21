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
    l = len(text) - 1
    buffer = []
    for i, char in enumerate(text):
        buffer.append(char)
        if char == ':' or char == '.' or char == '?':
            print("".join(buffer).strip())
            print()
            buffer = []
        elif i == l:
            print("".join(buffer).strip(), end="")
