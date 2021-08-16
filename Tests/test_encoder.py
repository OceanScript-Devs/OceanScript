import re
import string

from .maps import encoding_map as emap


def encode(content: str):
    content = content.lower()
    translator = content.maketrans(emap)
    new_content = content.translate(translator)
    return new_content
