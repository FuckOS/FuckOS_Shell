#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
	*************************** 
	--------description-------- 
 	 Autor: Kuro Kitu
 	 Description: FuckOS Shell Main
 	 Date: 2021-08-09 01:31:48
 	 LastEditors: Kuro Kitu
 	 LastEditTime: 2021-08-09 01:40:42

	***************************
"""

import os
import json
from os import *
from cmd import Cmd
from pyreadline import Readline
from pathlib import Path
from libs.time import *
from libs.clear import *
from libs.file import *
from libs.fuckflyos import *

version = 1.0
config = None
readline = Readline()

class FuckOSShell(Cmd):
    dir = Path.home()
    prompt = '\033[0;32;40mFuckOS>\033[0m '
    intro = """
    \033[0;32m
        ________  __________ ______  _____
       / ____/ / / / ____/ //_/ __ \/ ___/
      / /_  / / / / /   / ,< / / / /\__ \ 
     / __/ / /_/ / /___/ /| / /_/ /___/ / 
    /_/    \____/\____/_/ |_\____//____/ 
    
    Fuck flyos. The code is written like shit.
    \"EXIT\".lower ... LMAO

    FuckOS Shell V%s 
    Welcome! Type ? to list commands

    Now Time is %s

    \033[0m
    """ % (version, nowtime())

    def do_exit(self, arg):
        'exit: exit the application. Shorthand: x q Ctrl-D.'
        print("Bye")
        return True

    def do_time(self, arg):
        'time: Get current system time'
        print("Time: ", nowtime())

    def do_dir(self, arg):
        'die: syntax: dir path -- displaya list of files and directories'
        if not arg:
            print("\n".join(os.listdir(self.dir)))
        elif os.path.exists(arg):
            print("\n".join(os.listdir(arg)))
        else:
            print("No such pathexists.")

    def do_ls(self, arg):
        'ls: syntax: dir path -- displaya list of files and directories'
        self.do_dir(arg)

    def do_clear(self, arg):
        'clear: Clear Screen'
        clear()

    def do_cd(self, arg):
        'Working directory switching'
        self.dir = arg

    def do_pwd(self, arg):
        'Get current path'
        print(self.dir)

    def do_flyos(self, arg):
        'Fuck FlyOS'
        runflyos()

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Unknown command: {}\nPlease refer to the help list.".format(inp))


if __name__ == '__main__':
    config = json.loads(read_file('./configs/main.json'))
    print(type(config))
    if(config != None):
        clear()
        FuckOSShell().cmdloop()
