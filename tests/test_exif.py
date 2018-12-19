import os
from subprocess import CalledProcessError
from src.exif import Exif


os.chdir(os.path.dirname(__file__))


def test_exif_reads_valid_file():
    exif = Exif(["input/exif.jpg"])
    exif_data = exif.get("input/exif.jpg")
    assert exif_data['CreateDate'] == '2017:01:01 01:01:01'

def test_exif_handles_exception(mocker):
    mocker.patch('subprocess.check_output', side_effect=CalledProcessError(2, 'cmd'))
    exif = Exif(["not-existing.jpg"])
    exif_data = exif.get("not-existing.jpg")
    assert exif_data == None
