class OceanScriptError(Exception):
    """The base exception for all oceanscript related errors."""

    pass


class ForbiddenSquareError(OceanScriptError):
    """Raised when the forbidden 27th box is used."""

    def __init__(self):
        self.char = "_>..."
        super().__init__("Using '_>...' is forbidden")


class ParserError(OceanScriptError):
    """Raised when the decoder has trouble parsing."""

    def __init__(self, failed):
        self.failed = failed
        super().__init__("Failed to parse.")


class UnsupportedCharacterError(OceanScriptError):
    """Raised when an unsupported character is provided to the encoder."""

    def __init__(self, char):
        self.char = char
        super().__init__("Character '%s' is not supported" % char)
