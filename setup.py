import sys
from cx_Freeze import setup, Executable
from waterintake_tracker import __version__

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "PySide", "sqlite3"],
                     "excludes": ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
                                  'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
                                  'Tkconstants', 'Tkinter'],
                     "include_files": ["watericon.ico", "sql.schema"]
                     }

bdist_msi_options = {'add_to_path': False,
                     'initial_target_dir': r'[ProgramFilesFolder]\JagSoft\WaterTracker'
                     }

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(name="WaterTracker",
      version=__version__,
      description="Tracking water intake so you don't have to",
      author='Stuart Jackson',
      author_email='stuartrj1@gmail.com',
      options={"build_exe": build_exe_options, 'bdist_msi': bdist_msi_options},
      executables=[Executable("waterintake_tracker.py",
                              base=base,
                              shortcutName="WaterTracker",
                              shortcutDir="ProgramMenuFolder",
                              icon="watericon.ico",
                              targetName="WaterTracker.exe")])
