# Backdoor builder
from distutils.core import setup
import py2exe

setup(console=['backdoor.py'], options={'py2xee':{'bundle_fikes':1}}, zipfile=None,)

