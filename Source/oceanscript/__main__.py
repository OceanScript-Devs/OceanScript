#!/usr/bin/env python

import argparse

import oceanscript
from oceanscript.errors import OceanScriptError, ParserError


def format_exception(exc):
    ret = f"{exc.__class__.__name__}: {exc}"
    if isinstance(exc, ParserError):
        ret += " Try wrapping your decode argument with quotation marks."
    return ret


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

            try:
                encoded = oceanscript.encode(" ".join(args.encode))
            except OceanScriptError as exc:
                print(format_exception(exc))
                return
            else:
                message += title + encoded

        if args.decode:
            start = "\n" if message else ""
            try:
                decoded = oceanscript.decode("".join(args.decode))
            except OceanScriptError as exc:
                print(format_exception(exc))
                return
            else:
                message += start + "Decoded oceanscript: " + decoded

        print(message)

    return parse_args(args)


if __name__ == "__main__":
    main()
