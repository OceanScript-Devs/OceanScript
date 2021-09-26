import sys

import oceanscript
from oceanscript.errors import OceanScriptError, ParserError

ENCODE_HELP = "encode\n  Usage: oceanscript encode [arg]\n  Description: Encode normal text into oceanscript."
DECODE_HELP = "decode\n  Usage: oceanscript decode [arg]\n  Description: Decode oceanscript into normal text."
HELP_HELP = "help\n  Usage: oceanscript help [command=None]\n  Description: Shows this help menu, or help for a command."

HELP_MENU = f"""
OceanScript Help Menu
~~~~~~~~~~~~~~~~~~~~~

This is the command line interface for
encoding and decoding OceanScript. Here are 
the commands you can use:


{ENCODE_HELP}

{DECODE_HELP}

{HELP_HELP}


NOTICE:

When decoding, it's best to surround your text in 
quotes, so that it is parsed.
""".strip()

def format_cmd(cmd):
    return cmd[0].lower().lstrip('--')

def error(t):
    return "ERROR: " + t

def format_exception(exc):
    ret = f"{exc.__class__.__name__}: {exc}"
    if isinstance(exc, ParserError):
        ret += " Try wrapping your decode argument with quotation marks."
    return ret

def parse(argv):
    cmd = format_cmd(argv)
    if cmd not in ("encode", "decode", "help"):
        print(error(f"Unrecognized command '{cmd}'. Please refer to 'oceanscript help' for the list of commands."))
        return False
    if cmd == "help":
        if len(argv) > 1:
            try:
                message = globals()[f"{argv[1].upper().lstrip('--')}_HELP"]
            except KeyError:
                message = error(f"Help topic for '{' '.join(argv[1:])}' not found.")
        else:
            message = HELP_MENU
        
        print(message)
        return False

    if len(argv) == 1:
        print(error(f"The {cmd} command expected an argument. Run 'oceanscript help {cmd}' for more information."))
        return False

def transform(argv):
    cmd = format_cmd(argv)
    transform = getattr(oceanscript, cmd)
    try:
        transformed = transform(" ".join(argv[1:]))
    except OceanScriptError as e:
        message = format_exception(e)
        return
    else:
        text = f"{cmd.capitalize()} oceanscript:"
        if "\n" in transformed:
            text += "\n"
        else:
            text += " "
        message = text + transformed
    finally:
        print(message)

def main():
    argv = sys.argv[1:]
    if not argv:
        print(HELP_MENU)
        return
    if parse(argv) is False:
        return
    transform(argv)



if __name__ == "__main__":
    main()
