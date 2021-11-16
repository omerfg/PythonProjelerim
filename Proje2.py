# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:02:08 2021

@author: omrfrkg
"""

liste = [[1, 2], [3, 4], [5, 6, 7]]

def FuncReverse(liste):
    newList = []
    for i in liste:
        if (type(i) == list):
            i.reverse()
            newList.append(i)
        else:
            i.reverse()
            newList.append(i)
    print(newList)
    
FuncReverse(liste)
