#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   testInfer.py
@Time    :   2024/12/07 21:59:13
@Author  :   firstElfin 
@Version :   1.0
@Desc    :   None
'''
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "repo/repoExample/src/"))

from repo.repoExample.src.repoExample import infer

infer.infer()
