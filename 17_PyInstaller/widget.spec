# -*- mode: python -*-

block_cipher = None
import os
name = 'widget.exe'
a = Analysis(['widget.py'],
             pathex=[r'E:\\GoogleDrive\\3D\\Python\\education\\17_pyinstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.binaries += [('imageformats/qjpeg4.dll','C:/Users/mmiroshnichenko/AppData/Roaming/Python/Python27/site-packages/PySide/plugins/imageformats/qjpeg4.dll')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
		  a.binaries,
          a.zipfiles,
          a.datas,
          strip=None,
          upx=True,
          name=name,
		  debug=False,
          icon = 'icon.ico')

