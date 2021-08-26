import argparse
import sys

import oceanscript
from oceanscript.errors import OceanScriptError, ParserError


def main():
    parser = argparse.ArgumentParser(description="OceanScript encoder/decoder.", add_help=False)
    parser.add_argument("--encode", help="Encode a string into oceanscript", type=str, nargs="*")
    parser.add_argument("--decode", help="Decode oceanscript into a string.", type=str, nargs="*")

    args = parser.parse_args()

    def parse_args(args):
        cmds = vars(args)
        if all([value is None for value in cmds.values()]):
            print("Please provide either --encode, or --decode, with arguments.")
            print(
                "When decoding, it's wise to wrap your arguments with quotation marks to avoid parser errors."
            )
            return
        for arg, value in cmds.items():
            if value == []:
                print(f"The --{arg} argument takes exactly one argument, you didn't provide any.")
                return

        message = ""

        if args.encode:
            title = "Encoded oceanscript:"
            if len(args.encode) > 1:
                title += "\n"
            else:
                title += " "
            message += title + oceanscript.encode(" ".join(args.encode))

        if args.decode:
            start = "\n" if message else ""
            message += start + "Decoded oceanscript: " + oceanscript.decode("".join(args.decode))

        print(message)

    return parse_args(args)


if __name__ == "__main__":
    try:
        main()
    except OceanScriptError as exc:
        message = f"{exc.__class__.__name__}: {exc}"
        if isinstance(exc, ParserError):
            message += " Try wrapping your decode argument with quotation marks."
        print(message)
