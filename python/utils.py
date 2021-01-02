import itertools
import string


ALPHANUMERIC = string.hexdigits


def character_to_index(character):
    """
    :param character:
    :return:
    """
    return ALPHANUMERIC.index(character)


# Reference online
def index_to_character(index, character_length):
    """
    :param index:
    :param character_length:
    :return:
    """
    if character_length <= index:
        raise ValueError("Index out of range")
    else:
        return ALPHANUMERIC[index]


def get_next_combination(characters, character_length):
    """
    Returns next sequence of characters
    :param characters:
    :param character_length:
    :return:
    """
    if len(characters) <= 0:
        characters.append(index_to_character(0))
    else:
        characters[0] = index_to_character((character_to_index(characters[0]) + 1) % character_length)
        if character_to_index(characters[0]) is 0:
            return list(characters[0]) + get_next_combination(characters[1:], character_length)

    return characters


def permute(length=8, combinations=1000):
    """
    Generate different combinations of alphanumeric characters (hex)
    :param length:
    :param combinations:
    :return:
    """
    possible_combinations = ()