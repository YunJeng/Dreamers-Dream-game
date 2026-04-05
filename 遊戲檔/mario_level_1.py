#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario os for the NES.
"""

import sys
import pygame as pg
import subprocess
from data.main import main


if __name__=='__main__':
    try:
        main()
    finally:
        # ➤ 強制終止所有 ChucK 程式
        subprocess.run(["pkill", "-f", "chuck"])  # 適用於 macOS/Linux
        # Windows 使用 taskkill，可改成：
        # subprocess.run(["taskkill", "/f", "/im", "chuck.exe"])
        
        pg.quit()
        sys.exit()