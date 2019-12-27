#!/usr/bin/python3
# cbc.py

# Note: this is an interpreter, not a compiler - the name just sounds better this way.

import os
import sys

import translate as trt
import run_erase as rpf

if len(sys.argv) > 2 or len(sys.argv) == 1:
	print("Specify a file.")
	exit()

in_file = str(sys.argv[1])

if (in_file.endswith(".cboy")) is False:
	print("It's a good habit to use the .cboy file extension.")

in_file = sys.argv[1]

out_file = "text_out.py"

trt.translate_file(in_file)

rpf.run_file(out_file)

rpf.erase_file(out_file)