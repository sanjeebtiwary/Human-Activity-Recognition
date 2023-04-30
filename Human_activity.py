import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

setup(
    name="Human-Activity-Recognition",
    version="1.0",
    description="Real-time human activity recognition using computer vision and deep learning",
    options={"build_exe": build_exe_options},
    executables=[Executable("D:/Project/Human Activity Recognition/recognise_human_activity.py", base=None)]
)
