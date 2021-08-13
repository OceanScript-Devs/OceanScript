import re

from .maps import decoding_map
from .test_exceptions import ForbiddenSquareError, ParserError


def decode(i):
    i = i.strip()
    #  We want to strip the string BEFORE we handle
    #  line breaks.
    i = i.replace("\n", "\\n")
    #  oceanscript linebreaks convert to normal spaces.
    #  we need to enforce literal `\n` to avoid
    #  them from disappearing when splitting
    #  the string.
    builder = ""
    for group in re.split(r"(\\n)|([\^~_])([>\-<])(\.{1,3})", i):
        if not group:
            builder += " "
        else:
            builder += group
    message = ""
    for x in builder.split():
        try:
            message += decoding_map[x]
        except KeyError:
            if x == ForbiddenSquareError.char:
                raise ForbiddenSquareError() from None
            raise ParserError(x)

    return message
