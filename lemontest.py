from __future__ import print_function
import imp


if __name__ == "__main__":
    lw = imp.load_source("lw", "./lemonwrap")
    lw16 = imp.load_source("lw16", "./lemonwrap16")

    for m in [lw, lw16]:
        for i in range(len(m.LEMONGRAB)):
            print(m.recondition(m.LEMONGRAB[i]))
