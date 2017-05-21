# Requires Python 3; tested with Python 3.6

from base64 import b64encode
import sys
from zlib import compress


LEMON_LENGTH = 70


def lemoncode(filename):
    with open(filename, "rb") as f:
        lemon = f.read()
    squeezed_lemon = compress(lemon, level=9)
    lemonjuice = b64encode(squeezed_lemon).decode("ascii")
    sliced_lemon = [
        lemonjuice[i:i + LEMON_LENGTH]
        for i in range(0, len(lemonjuice), LEMON_LENGTH)
        ]
    fancy_lemon = "\n".join(map('"{:s}"'.format, sliced_lemon))
    return fancy_lemon


if __name__ == "__main__":
    print(lemoncode(sys.argv[1]))
