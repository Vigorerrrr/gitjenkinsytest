# !/usr/bin python3                                 
# encoding   :utf-8 -*-                                                          
# @software  :PyCharm     
# @file      :run.py
import time
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,BASE_DIR)
import pytest
import time
timestr = str(int(time.time()))
html_path = "--html=Output/test.{}.html".format(timestr)
pytest.main([html_path,"--alluredir=allurereport/allure"])


