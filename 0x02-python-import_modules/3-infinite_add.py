#!/usr/bin/python3
import sys
numbers = sys.argv[1:]
sum_ = 0
for i in numbers:
    sum_ += int(i)
print(sum_)
