#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
# File Name: 21-doc_test.py
# Author: Ajioy
# mail: ajioy@hotmail.com

import re
m = re.search('(?<=abc)def', 'abcdef')
print m.group(0)

def abs(n):
  '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
  return n if n >= 0 else (-n)
