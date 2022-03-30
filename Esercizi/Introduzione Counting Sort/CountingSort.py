# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:35:52 2021

@author: Matte
"""

def CountingSort(a):
    uno, due, tre, i = 0, 0, 0, 0
    
    while i < len(a):
        if a[i] == 'uno':
            uno += 1
        elif a[i] == 'due':
            due += 1
        else:
            tre += 1
        i += 1
            
    i = 0
    while i < len(a):
        if i < due:
            a[i] = 'due'
        elif i < due + tre:
            a[i] = 'tre'
        else:
            a[i] = 'uno'
        i += 1
    
        
        

a = ['tre','tre','uno', 'due', 'due', 'tre', 'uno']
CountingSort(a)
print(a)