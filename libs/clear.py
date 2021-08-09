#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
	*************************** 
	--------description-------- 
 	 Autor: Kuro Kitu
 	 Description: 
 	 Date: 2021-08-09 04:31:52
 	 LastEditors: Kuro Kitu
 	 LastEditTime: 2021-08-09 04:31:53

	***************************
"""

import platform, os


def clear():
    clear_cmd = "cls" if platform.system() == 'Windows' else "clear"
    os.system(clear_cmd)
