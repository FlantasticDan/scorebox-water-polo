# PyInstaller SPEC Files

### One Directory
```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['flask/main.py'],
             pathex=['flask'],
             binaries=[],
             datas=[('flask/templates', 'templates'), ('flask/static', 'static')],
             hiddenimports=[
                 'engineio.async_drivers.eventlet',
                 'eventlet.hubs.epolls',
                 'eventlet.hubs.kqueue',
                 'eventlet.hubs.selects',
                 'dns.dnssec',
                 'dns.e164',
                 'dns.hash',
                 'dns.namedict',
                 'dns.tsigkeyring',
                 'dns.update',
                 'dns.version',
                 'dns.zone'
                 ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='flask')
```

### One File
```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['flask/main.py'],
             pathex=['flask'],
             binaries=[],
             datas=[('flask/templates', 'templates'), ('flask/static', 'static')],
             hiddenimports=[
                 'engineio.async_drivers.eventlet',
                 'eventlet.hubs.epolls',
                 'eventlet.hubs.kqueue',
                 'eventlet.hubs.selects',
                 'dns.dnssec',
                 'dns.e164',
                 'dns.hash',
                 'dns.namedict',
                 'dns.tsigkeyring',
                 'dns.update',
                 'dns.version',
                 'dns.zone'
                 ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ScoreBox-WaterPolo-CTS-v1.0.0',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
```