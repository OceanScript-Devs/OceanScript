import re
import string

from .maps import encoding_map as emap

def encode(content: str):
    content = content.lower()

    encoding_map = emap.copy()
    # We want to modify our encoding map here
    # to support punctuation.
    for i in string.punctuation:
        encoding_map[i] = f"[{i}]"
    translator = content.maketrans(encoding_map)
    new_content = content.translate(translator)
    return re.sub(r"\]\[", "", new_content)
