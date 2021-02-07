import argparse
import errno
import os
from concurrent.futures import ThreadPoolExecutor
import pytest


class GenerateAtbash:
	def __init__(self):
		self.transform = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
									   "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba")
		self.get_files()

	def start(self):
		with ThreadPoolExecutor() as ex:
			ex.map(self.do_cipher, self.files)

	def do_cipher(self, file):
		with open(file, "r") as readfile, open(
				os.path.join(ENC_PATH, f"{file.split('.')[0]}_encrypted.{file.split('.')[1]}"), "w+") as writefile:
			for x in readfile.readlines():
				writefile.write(x.translate(self.transform))

	def get_files(self):
		parser = argparse.ArgumentParser()
		parser.add_argument("--file", "-f", type=str, required=True, nargs='+')
		args = vars(parser.parse_args())
		self.files = args.get("file")


def make_dir(*paths):
	# Creates all required directories if not present, mentioned in the path.
	for pt in paths:
		if not (os.path.isdir(pt)):
			try:
				os.makedirs(pt, mode=0o777, exist_ok=True)
			except OSError as exception:
				if exception.errno != errno.EEXIST:
					raise


if __name__ == "__main__":
	ENC_PATH = os.path.join(os.getcwd(), "Encrypted Files")
	make_dir(ENC_PATH)
	obj = GenerateAtbash()
	obj.start()
