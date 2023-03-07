#!/usr/bin/python3
def uppercase(str):
    nums = list(range(65, 91))
    new_str = ""

    for i in str:
        if ord(i) in nums:
            new_str+=i
        else:
            new_str+=chr(ord(i))

        
