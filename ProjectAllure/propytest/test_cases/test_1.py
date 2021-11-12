# !/usr/bin python3                                 
# encoding   :utf-8 -*-                                                          
# @software  :PyCharm     
# @file      :test_1.py
import pytest


def add(a, b):
    return a + b


def teststr():
    """测试字符串"""
    a, b = '1', '2'
    assert add(a, b) == '12'
    print("测试字符串")


def test_int():
    """测试整型"""
    a, b = 1, 2
    assert add(a, b) == 3
    print("测试整型")


class TestSequence:
    def test_list(self):
        assert add([1], [2]) == [1, 2]

    def test_tuple(self):
        assert add((1,), (2,)) == (1, 2)


if __name__ == '__main__':
    pytest.main()










