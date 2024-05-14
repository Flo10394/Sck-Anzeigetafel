# -*- mode: python ; coding: utf-8 -*-

import sys
from os import path
from PyInstaller.building.build_main import Analysis

python_interpreter = sys.executable
site_packages = os.path.join(os.path.dirname(python_interpreter), "..", "Lib", "site-packages")
block_cipher = None


added_files = [ ]
added_binaries = [ ]

a = Analysis(
    ['sck_screen.py'],
    pathex=['./../..'],
    binaries=added_binaries,
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='sck_screen_tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='gen_version_info.txt'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SCK Screen Tool',
)
