"""
Module for text_indentation function.
Prints a text with 2 new lines after each '.', '?', and ':' character.
"""
#!/usr/bin/python3


def text_indentation(text):
    """
    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        i = 0
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(char, end='')
            i += 1
