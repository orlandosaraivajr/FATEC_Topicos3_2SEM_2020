#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
StrKeyDict
Extraido do capítulo 3 do livro "Python Fluente"
"""

import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if  isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item

