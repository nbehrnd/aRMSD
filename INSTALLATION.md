Installation details
------------------------

aRMSD uses several packages that are actively developed and continuously change in the future. Therefore keeping track of changes in other packages is important to ensure that aRMSD will continue to work with newer package versions. The program was developed and tested with the following versions of the directly used thrid party packages. 

**Module versions**

         - numpy 1.11.1 / 1.12
         - matplotlib 1.5.3 / 2.0
         - vtk 6.2.0 / 7.0
         - future 0.16.0
         - uncertainties 3.0.1
         - cython 0.25.2
         - openbabel 2.4.1

Due to changes from vtk 5 to 6, aRMSD does not support older vtk version than 6.2 and a backwards compatibility to the older vtk 5 engine is not planned (unless it is frequently requested).

**Compilation arguments**

The following arguments can be passed to the installation script and specify the usage of Cython and openbabel in the compilation. All arguments are optional and if none are given neither Cython nor openbabel will be used. The specification of the C compiler may not be needed if your defaults are properly set, however setting it explicitly should ensure a successful installation.

         - --use_cython (True / False)
         - --cython_compiler (any valid C compiler used by Cython, e.g. msvc)
         - --use_openbabel (True / False)
         - --overwrite (True / False)

During the installation, the existence of an openbabel hook file in the PyInstaller hook path is checked. If no hook exists, a respective file will be created. In case of an existing hook, the file can be overwritten if the --overwrite variable is set to True.


Future developments
------------------------

Several new features and improvements are planned which will hopefully be continuously added in the future, some of which are:

         - Better 3D rendering for large molecules (>2000 atoms)
         - Reduction of matching errors through improved cost matrices
         - Improvements for 2D and 3D plots (mostly text annotation)
         - Better formatting for the output and improved [Blender] (http://www.blender.org) interface
         - Structural interpolation in internal coordinates
         - Better support of substructures

Any ideas are always welcome and requested features will be added if time allows it.

## Hints for the installation in Windows 10/64bit

With current Python 3.13, it is not possible to successfully resolve the
dependencies of `aRMSD` with `pip` reaching out to the public repository of the
PyPI.  Reasons can be due to a change of syntax, for instance the initialization
of arrays `matplotlib` introduced in 2024.  Another that it seems impossible to
fetch _a complete_ set of the dependencies _sufficiently old_ to successfully
interact with each other, and successfully support `aRMSD`.  Some of the modules
in question rely not only on interpreted, but compiled source code; the later
usually renders a Python wheel specific to a particular operating system.

The sequence of instructions below describe an installation of `aRMSD` in
Windows 10/64bit; these do not alter an already existing installation of
Python 3.13.

1. Fetch the content of both
   [aRMSD](https://github.com/nbehrnd/aRMSD)
   (about 45MB) and
   [aRMSD-minimalWindowsSupport](https://github.com/nbehrnd/aRMSD-minimalWindowsSupport)
   (about 292MB) from the corresponding GitHub pages.
1. The offical site of
   [Python.org](https://www.python.org)
   provides many relases of Python interpreters.  For the purpose of this
   manual, fetch the 32bit msi installer for Windows of
   [python-2.7.15.msi](https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi)
   published in May 2018.
   Visit the download page dedictated to the
   [Windows operating system](https://www.python.org/downloads/windows)
   for additional information and checksums.
1. While running the .msi installer, a new folder `C:\Python27` is
   created.  To keep the access to your default Python interpreter from your
   shell, at this stage, Python 2.7 _must not_ be added to Windows' `PATH`
   variable.  Instead, write a "link file"  `python27.bat` with the content of

   ```
   @echo off
   C:\Python27\python.exe%*
   ```

   to indicate the location of the interpreter.  You then can lauch the
   executable from `cmd.exe` or Windows's PowerShell locally by `python27.bat`.

   As an option, you may add the location of _this link file_ to Windows' `PATH`
   variable; then, the command `python27` to `cmd.exe` or PowerShell provides
   you systemwide access to the old Python interpreter.
1. Presuming you have (a copy of) the link file in the folders of the Python
   wheels fetched, install them one after the other, for instance by the command

   ```
   python27.bat -m install "openbabel-2.4.1-cp27m-wind32.whl"
   ```

   Note: at least in the case of `matplotlib`, `pip` successfully resolves a
   dependency (of `matplotlib`).

To launch `aRSMD`, copy-paste for instance the test files `M1.xyz` and `M2.xyz`
about two conformers of benzamide into the folder containing `aRMSD.py` and its
supporting modules.  If you didn't add the link file to Windows, equally paste
a copy in this current working directory, too and launch the program by

```
python27.bat aRMSD.py
```

Proceed as outlined by the program's help or/and documentation.  The support of
aRMSD's anaglyph representations may depend on the interaction between the VTK
library on one, and chip set/graphics card setup of the computer use on the
other hand.
