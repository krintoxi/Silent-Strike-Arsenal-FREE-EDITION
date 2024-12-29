# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['SSA.py'],
    pathex=[],
    binaries=[],
    datas=[('scripts/Logo.png', 'config'), ('scripts/Logo.png', 'config'), ('tools/VSCAN', 'tools/VSCAN--hidden-import=tkinter'), ('tools', 'tools'), ('scripts', 'scripts')],
    hiddenimports=['PIL.ImageTk', 'PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SSA',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
