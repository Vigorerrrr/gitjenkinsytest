# !/usr/bin python3                                 
# encoding   :utf-8 -*-                                                          
# @software  :PyCharm     
# @file      :run.py
import time

import pytest
import time
timestr = str(int(time.time()))
html_path = "--html=Output/test.{}.html".format(timestr)
pytest.main([html_path,"--alluredir=allurereport/allure"])


