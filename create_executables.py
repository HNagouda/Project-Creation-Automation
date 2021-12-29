"""
.py to .exe converter
    converts the scripts `open.py` and `create.py` into executable files
    The executables can be easily invoked through a CLI

Note: This script is generalized and can be used anywhere
      Simply change the contents of the `files_to_convert" list
"""

import os
import shutil
from threading import Thread

class py_to_exe():
    def __init__(self):
        self.files_to_convert = ['creator.py', 'open.py'] # List of all .py files to be converted

    def create_executable(self):     
        for py_filename in self.files_to_convert:   
            os.system(f"pyinstaller {py_filename} -F")

            shutil.copyfile(f"./dist/{py_filename.split(sep='.')[0]}.exe", f"./{py_filename.split('.')[0]}.exe")

            shutil.rmtree('./dist')
            shutil.rmtree('./build')
            os.remove(f"./{py_filename.split(sep='.')[0]}.spec")

    def run_all(self):
            Thread(target = self.create_executable()).start()

if __name__ == "__main__":
    py_to_exe().run_all()
