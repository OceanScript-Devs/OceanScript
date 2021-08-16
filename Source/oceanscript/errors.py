class OceanScriptError(Exception):
    """The base exception for all oceanscript related errors."""

    pass


class ForbiddenSquareError(OceanScriptError):
    """This exception is now deprecated with the addition of numbers."""

    def __init__(self):
        import warnings

        warnings.warn(
            "ForbiddenSquareError is no longer used and will be removed in a future release.",
            category=DeprecationWarning,
            stacklevel=3,
        )
        super().__init__("Using '_>...' is forbidden")  # no longer forbidden


class ParserError(OceanScriptError):
    """Raised when the decoder has trouble parsing."""

    def __init__(self):
        super().__init__("Failed to parse.")


class UnsupportedCharacterError(OceanScriptError):
    """Raised when an unsupported character is provided to the encoder."""

    def __init__(self, char):
        self.char = char
        super().__init__("Character '%s' is not supported" % char)
