#!/usr/bin/python3
import sys
args_ = sys.argv[1:]
if len(args_) == 1:
    print("{} argument".format(1))
else:
    print("{} arguments".format(len(args_)))
i = 1
for arg_ in args_:
    print("{}: {}".format(i, arg_))
    i+=1
