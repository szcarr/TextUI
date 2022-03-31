import os
import platform

import fileHandling as fh
import debug

hei = os.popen("where /r C:\ *AppData*").read()
print(hei)