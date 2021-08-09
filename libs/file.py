#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
	*************************** 
	--------description-------- 
 	 Autor: Kuro Kitu
 	 Description: 
 	 Date: 2021-08-09 04:56:43
 	 LastEditors: Kuro Kitu
 	 LastEditTime: 2021-08-09 04:56:44

	***************************
"""

def read_file(path):
    data = None
    with open(path, 'r',encoding='utf8') as fp:
        data = fp.read()
        fp.close()

    return data

def write_file(path, data):
    with open(path, "w+", encoding='utf8') as fp:
        fp.write(data)
        fp.flush()
        fp.close()