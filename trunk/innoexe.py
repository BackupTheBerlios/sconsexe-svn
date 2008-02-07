'''Find where InnoSetup exeutable is'''

__author__ = "Miki Tebeka <miki.tebeka@gmail.com>"

from _winreg import OpenKeyEx, EnumKey, QueryValueEx, CloseKey, \
    HKEY_LOCAL_MACHINE
from os.path import join
from itertools import count

uninst = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
key = OpenKeyEx(HKEY_LOCAL_MACHINE, uninst)
i = 0
for i in count(): # When i will becode too large we'll get WindowsError
    innokey = EnumKey(key, i)
    if "Inno Setup" in innokey:
        break
ikey = OpenKeyEx(key, innokey)
instdir, type = QueryValueEx(ikey, "InstallLocation")
CloseKey(ikey)
CloseKey(key)

print join(instdir, "ISCC.exe")
