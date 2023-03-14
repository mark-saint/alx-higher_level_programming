#!/usr/bin/python3
import hidden_4
for i in hidden_4.__dir__():
    if i.startswith("__"):
        continue
    print("{}".format(i))
