# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:05:53 2019

@author: KarthikM
"""

the_file = open('sketch.txt')

for each_line in the_file:
    print(each_line)

the_file.close()