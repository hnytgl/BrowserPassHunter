#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BrowserPassHunter v1.0 - Browser Password Recovery Tool
Supports 25+ browsers on Windows
"""
import marshal, types, sys, os, json, base64, sqlite3, shutil
import tempfile, csv, time, platform
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Optional, Tuple, Any
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import win32crypt
from win32crypt import CryptUnprotectData

try:
    from Crypto.Cipher import DES3
    from Crypto.Hash import SHA, HMAC, SHA1
    from Crypto.Protocol.KDF import PBKDF2
except ImportError:
    DES3 = SHA = HMAC = SHA1 = PBKDF2 = None

# Load compiled module
PYC = Path(__file__).parent / '__pycache__' / 'browser_pass_hunter.cpython-312.pyc'
if not PYC.exists():
    print("Error: cache not found. Re-run from the original .py file.")
    sys.exit(1)

with open(PYC, 'rb') as f:
    for _ in range(4): f.read(4)
    code = marshal.load(f)

mod = types.ModuleType('browser_pass_hunter')
mod.__file__ = str(__file__)
sys.modules['browser_pass_hunter'] = mod

# Populate module globals
for k, v in {'os':os,'json':json,'base64':base64,'sqlite3':sqlite3,
             'shutil':shutil,'tempfile':tempfile,'csv':csv,'time':time,
             'platform':platform,'Path':Path,'defaultdict':defaultdict,
             'List':List,'Dict':Dict,'Optional':Optional,'Tuple':Tuple,
             'Any':Any,'AESGCM':AESGCM,'win32crypt':win32crypt,
             'CryptUnprotectData':CryptUnprotectData,
             'DES3':DES3,'SHA':SHA,'HMAC':HMAC,'SHA1':SHA1,'PBKDF2':PBKDF2,
             'collections':__import__('collections'),
             'traceback':__import__('traceback')}.items():
    setattr(mod, k, v)

# pycryptodome caps
mod.HAS_PYCRYPTODOME = DES3 is not None
mod.HAS_WIN32CRYPT = True
mod.HAS_CRYPTOGRAPHY = True

exec(code, mod.__dict__)

# Patch: More helpful v20 error message
orig_decrypt = mod.ChromeProcessor._decrypt_chrome_password

def patched_decrypt(self, encrypted_value):
    result = orig_decrypt(self, encrypted_value)
    if result and result.startswith('[Decrypt failed:') and 'v20' in result:
        result = '[Decrypt failed: Chrome v20+ App-Bound encryption. View passwords at chrome://settings/passwords]'
    return result

mod.ChromeProcessor._decrypt_chrome_password = patched_decrypt

if __name__ == "__main__":
    mod.main()
