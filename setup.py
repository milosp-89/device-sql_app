from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup (
    windows = [
        {
            "script": 'ds.py',     
            "icon_resources": [(0, "ds.ico")]
        }
    ],
)