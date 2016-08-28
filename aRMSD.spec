block_cipher = None

import sys
import os

folder = os.getcwd()  # Get current working directory

binaries = []

extra_datas = []

excludes = ['_ssl', '_hashlib', 'PySide', '_gtkagg', '_tkagg', '_wxagg', '_qt5agg', 'bsddb', 'curses', 'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl', 'Tkconstants', 'Tkinter', 'wx', '_Qt5Agg']

hiddenimports = ['matplotlib', 'vtk', 'uncertainties']


a = Analysis(['aRMSD.py'],
             pathex=[folder],
             binaries=binaries,
             datas=extra_datas,
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=excludes,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

# Determine platform and bitsize
platform = ''
name = 'aRMSD'

if sys.platform == 'win32':

    platform = 'Win'

if sys.maxsize > 2 ** 32:

    platform += '64'

else:
    
    platform += '32'

# Determine version and append it to file name
from aRMSD import __aRMSD_version__

name += '_{}_{}'.format(__aRMSD_version__, platform)

# Exclude TK and TCL .dlls
a.binaries = a.binaries - TOC([('tcl85.dll', None, None), ('tk85.dll', None, None)])
    
# Setup pyz
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=name,
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon=folder+'\\aRMSD_icon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=name)