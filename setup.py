from cx_Freeze import setup, Executable

setup(
    name="lights-out",
    executables=[Executable("lights-out.py", base="Win32GUI")],
)
