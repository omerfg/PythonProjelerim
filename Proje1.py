# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:02:08 2021

@author: omrfrkg
"""
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

str_list = str(liste)
str_list = str_list.replace("[", "").replace(("]"),"")
result = str_list.split(",")

print(result)
