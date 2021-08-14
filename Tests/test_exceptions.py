class OceanScriptError(Exception):
    pass


class ForbiddenSquareError(OceanScriptError):
    def __init__(self):
        self.char = "_>..."
        super().__init__("Using _>... is forbidden")


class ParserError(OceanScriptError):
    def __init__(self, failed):
        self.failed = failed
        super().__init__("Failed to parse '%s'" % failed)


class UnsupportedCharacterError(OceanScriptError):
    def __init__(self, char):
        self.char = char
        super().__init__("Character %s is not supported" % char)


class PunctuationBlockError(OceanScriptError):
    pass
