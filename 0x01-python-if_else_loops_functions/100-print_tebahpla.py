#!/usr/bin/python3
reversed_list = list(reversed(list(range(97, 123))))
is_lower = True
for i in reversed_list:
    if is_lower:
        i = chr(i)
        is_lower = False
    else:
        i = chr(i - 32)
        is_lower = True
    print("{}".format(i), end='')
