from subprocess import check_output, CalledProcessError, STDOUT
import json
import sys


class Exif(object):
    def __init__(self, files):
        self.data = {}
        output = None
        try:
            string_files = '"{0}"'.format('" "'.join(files))
            output = check_output('exiftool -time:all -mimetype -j -q -q %s; exit 0' % string_files, sys.stderr==STDOUT, shell=True).decode('UTF-8')
        except (CalledProcessError, UnicodeDecodeError):
            pass
            
        if output:
            data = json.loads(output)
            for file in data:
                self.data[file["SourceFile"]] = file

    def get(self, file):
        return self.data.get(file)
        
    
