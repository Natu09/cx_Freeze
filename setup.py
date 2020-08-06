import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

executables = [Executable("exe1.py", base=base),
               Executable("exe2.py", base=base)]

# options = {'build_exe': {'init_script':'Console'}}

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="CX_FREEZE",
      version="0.1",
      description="My GUI application!",
      options={"build_exe": build_exe_options},
      executables=executables)
