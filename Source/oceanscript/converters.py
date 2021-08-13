import re as _re
import string as _string

from .errors import ForbiddenSquareError, ParserError, UnsupportedCharacterError

_maps = {
    "encoding_map": {
        " ": "\n",
        "a": "^<.",
        "b": "^-.",
        "c": "^>.",
        "d": "~<.",
        "e": "~-.",
        "f": "~>.",
        "g": "_<.",
        "h": "_-.",
        "i": "_>.",
        "j": "^<..",
        "k": "^-..",
        "l": "^>..",
        "m": "~<..",
        "n": "~-..",
        "o": "~>..",
        "p": "_<..",
        "q": "_-..",
        "r": "_>..",
        "s": "^<...",
        "t": "^-...",
        "u": "^>...",
        "v": "~<...",
        "w": "~-...",
        "x": "~>...",
        "y": "_<...",
        "z": "_-...",
    },
    "decoding_map": {
        "\\n": " ",
        "^<.": "a",
        "^-.": "b",
        "^>.": "c",
        "~<.": "d",
        "~-.": "e",
        "~>.": "f",
        "_<.": "g",
        "_-.": "h",
        "_>.": "i",
        "^<..": "j",
        "^-..": "k",
        "^>..": "l",
        "~<..": "m",
        "~-..": "n",
        "~>..": "o",
        "_<..": "p",
        "_-..": "q",
        "_>..": "r",
        "^<...": "s",
        "^-...": "t",
        "^>...": "u",
        "~<...": "v",
        "~-...": "w",
        "~>...": "x",
        "_<...": "y",
        "_-...": "z",
    },
}


def encode(content: str):
    """Encode normal text into oceanscript.

    This function only takes a-Z and whitespace, as that's the only form that oceanscript supports.
    Capitalization is ignored. You should provide a string, of any length.
    The return value will be in oceanscript.

    Example Usage:

    import oceanscript
    oceanscript.encode('hello')
    >>> _-.~-.^>..^>..~>..
    """
    content = content.lower()
    for character in content:
        if not character in _string.ascii_letters + " ":
            raise UnsupportedCharacterError(character)

    translator = content.maketrans(_maps["encoding_map"])
    return content.translate(translator)


def decode(content: str):
    """Decode oceanscript into normal text.

    This function takes valid oceanscript which you can retrieve from the encode method.
    A normalized string will be returned, in full lowercase.

    Example Usage:

    import oceanscript
    oceanscript.encode("_-.~-.^>..^>..~>..")
    >>> 'hello'
    """
    content = content.strip()
    content = content.replace("\n", "\\n")

    formation = ""
    for x in _re.split(r"(\\n)|([\^~_])([>\-<])(\.{1,3})", content):
        if not x:
            formation += " "
        else:
            formation += x

    ret = ""

    for x in formation.split():
        try:
            ret += _maps["decoding_map"][x]
        except KeyError:
            if x == ForbiddenSquareError.char:
                exc = ForbiddenSquareError()
            else:
                exc = ParserError(x)
            raise exc from None

    return ret
