class OceanScriptError(Exception):
    pass


class ParserError(OceanScriptError):
    def __init__(self, failed):
        self.failed = failed
        super().__init__("Failed to parse '%s'" % failed)


class UnsupportedCharacterError(OceanScriptError):
    def __init__(self, char):
        self.char = char
        super().__init__("Character %s is not supported" % char)
