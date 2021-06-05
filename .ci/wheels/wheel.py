import subprocess
import sys

import setup_python

version = sys.argv[1]
interpreter = setup_python(version)
process = subprocess.check_call([interpreter, "install.py"])
