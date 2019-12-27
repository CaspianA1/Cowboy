# run_erase.py

import os

def run_file(file_name):

	if file_name.endswith(".py"):
		pass
	else:
		file_name += ".py"

	file_name = file_name.lower().strip()

	os.system(f"python3 {file_name}")

def erase_file(file_name):
	with open(f"{file_name}", "w") as f: pass