#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_ = sys.argv[1:]
    if len(args_) == 1:
        print("1 argument:")
    elif len(args_) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(args_)))
    i = 1
    for arg_ in args_:
        print("{}: {}".format(i, arg_))
        i += 1
