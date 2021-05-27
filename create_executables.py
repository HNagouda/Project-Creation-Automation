"""
.py to .exe converter
    converts the scripts `open.py` and `create.py` into executable files
    The executables can be easily invoked through a CLI

Note: This script is generalized and can be used by anyone, anywhere
      Simply change the contents of the `files_to_convert" list
"""

import os
import shutil

files_to_convert = ['create.py', 'open.py'] # List of all .py files to be converted

def create_executable(py_filename):        
    os.system(f"pyinstaller {py_filename} -F")

    shutil.copyfile(f"./dist/{py_filename.split(sep='.')[0]}.exe", f"./{py_filename.split('.')[0]}.exe")

    shutil.rmtree('./dist')
    shutil.rmtree('./build')
    os.remove(f"./{py_filename.split(sep='.')[0]}.spec")


if __name__ == "__main__":
    for file in files_to_convert:
        create_executable(str(file))
