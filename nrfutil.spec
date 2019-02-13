# -*- mode: python -*-

import importlib
import os
import sys

block_cipher = None

module = importlib.import_module("pc_ble_driver_py")
mod_dir = os.path.dirname(module.__file__)
shlib_dir = os.path.join(os.path.abspath(mod_dir), 'lib')
hex_dir = os.path.join(os.path.abspath(mod_dir), 'hex')

binaries = [(shlib_dir, 'lib'), (hex_dir, 'pc_ble_driver_py/hex')]

# ant is relevant for windows only
if (sys.platform == "win32"):
    module_ant = importlib.import_module('antlib')
    mod_dir_ant = os.path.dirname(module_ant.__file__)
    shlib_dir_ant = os.path.abspath(mod_dir_ant)
    binaries.append((shlib_dir_ant, '.'))


nrfutil_path = os.path.dirname(os.path.abspath(SPEC))
binaries.append((nrfutil_path + "\\libusb\\x86", "\\libusb\\x86"))
binaries.append((nrfutil_path + "\\libusb\\x64", "\\libusb\\x64"))


a = Analysis(['nordicsemi/__main__.py'],
             binaries=binaries,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='nrfutil',
          debug=False,
          strip=False,
          upx=True,
          console=True)
