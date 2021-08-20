import argparse

import oceanscript

parser = argparse.ArgumentParser(description="OceanScript encoder/decoder.", add_help=False)
parser.add_argument("--encode", help="Encode a string into oceanscript", type=str)
parser.add_argument("--decode", help="Decode oceanscript into a string.", type=str)
args = parser.parse_args()


def parse(args):
    var_values = list(vars(args).values())
    if not any(var_values):
        print("Please provide either --encode, or --decode, with arguments.")
        return
    if all(var_values):
        print("Please only encode or decode.")
        return

    message = ""

    if args.encode:
        title = "Encoded oceanscript:"
        if len(args.encode) > 1:
            title += "\n"
        else:
            title += " "
        message += title + oceanscript.encode("".join(args.encode))

    if args.decode:
        print("".join(args.decode))
        message += "Decoded oceanscript: " + oceanscript.decode("".join(args.decode))

    print(message)


parse(args)
