#!/usr/bin/python3
"""
function text_indentation
"""

def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        for char in text:
            print("{}".format(char), end="")
            if char in [".", "?", ":"]:
                print("\n")
