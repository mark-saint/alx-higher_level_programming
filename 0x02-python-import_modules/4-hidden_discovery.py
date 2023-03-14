#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in hidden_4.__dir__():
        if i.startswith("__"):
            continue
        print("{}".format(i))
