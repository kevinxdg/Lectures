#coding=utf-8

import sys
import os

# ------------------------------------
# 确定主要工作目录
lib_dir = r'D:\Workspace\PythonLibs\ObjectLib'
sys.path.append(lib_dir)
#-------------------------------------

cur_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(cur_dir + r'\..')

data_dir = parent_dir + r'\Data'          # 数据目录

arcskills_dir = parent_dir + r'\ArcSkills'

syntax_dir = parent_dir + r'\BasicSyntax'

landuse_dir = parent_dir + r'\Landuse'

libs_dir = parent_dir + r'\Libs'

MXY_dir = parent_dir + r'\MXY'

temp_dir = parent_dir + r'\Temp'

XTL_dir = parent_dir + r'\XTL'

ZYY_dir = parent_dir + r'\ZYY'

