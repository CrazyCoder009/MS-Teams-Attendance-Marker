from cx_Freeze import setup, Executable

setup(name='MS Attendance',
	  version='0.1',
	  description='Arrange your Attendance',
	  executables = [Executable("MS Attendance.py")])