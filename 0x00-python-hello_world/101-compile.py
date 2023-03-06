#!/usr/bin/python3
import py_compile
import sys
filename = sys.argv[1]
split_ = filename.split('.')[0]
new_filename = split_ + '.pyc'
py_compile.compile(filename, cfile=new_filename)
