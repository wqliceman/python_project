# -*- coding: utf-8 -*-
__author__ = 'wqliceman'

from distutils.core import setup
import py2exe
import glob

INCLUDES = []
options = {'py2exe':
    {
        "compressed": 1,
        "optimize": 2,
        "bundle_files": 1,
        "includes": INCLUDES,
        "dist_dir": "dist"
    }
}

setup(options=options,
      version="1.0",
      name="点个评",
      description="大众点评团购订单",
      zipfile=None,
      console=[{'script': 'getDianpingOrder.py', 'icon_resources': [(1, 'logo.ico')]}],
      data_files=[("capcha", "owner", "logo.ico")]
      )
