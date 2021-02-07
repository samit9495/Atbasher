import pytest
import os


@pytest.fixture()
def init_runcode(filename):
	global name
	name = filename
	os.system("python atbasher.py -f {}".format(" ".join(filename)))


def test_filegenerated(init_runcode):
	path = os.path.join(os.getcwd(), "Encrypted Files")
	files = os.listdir(path)
	for file in name:
		assert f"{file.split('.')[0]}_encrypted.{file.split('.')[1]}" in files, "File not Generated"


def test_filetype(filename):
	assert filename, "No Filename provided in commandline"

	for n in filename:
		assert n.split(".")[1] == "txt", "Invalid File Format"
