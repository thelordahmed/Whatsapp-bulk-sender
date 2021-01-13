from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, targetName = 'WhatsApp Bulk Sender')
]

setup(name='Whatsapp Bulk Sender',
      version = '2.5.2',
      description = 'Developed by LorDAhmeD',
      options = dict(build_exe = buildOptions),
      executables = executables)
