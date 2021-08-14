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
    formation = ""
    for x in re.split(r"(\\n)|(\[.+\])|([\^~_])([>\-<])(\.{1,3})", i):
        if not x:
            formation += " "
        else:
            formation += x

    ret = ""

    for x in formation.split():
        try:
            ret += decoding_map[x]
        except KeyError:
            if re.match(r"\[.+\]", x):
                ret += re.sub(r"\[(.+)\]", r"\1", x)
                continue
            if x == "_>...":
                exc = ForbiddenSquareError()
            else:
                exc = ParserError(x)
            raise exc from None

    return ret