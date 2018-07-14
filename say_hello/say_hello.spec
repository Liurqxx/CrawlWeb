# -*- mode: python -*-

block_cipher = None


a = Analysis(['say_hello.py'],
             pathex=['C:\\Users\\29905\\Desktop\\say_hello'],
             binaries=[],
             datas=[],
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
          name='say_hello',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
