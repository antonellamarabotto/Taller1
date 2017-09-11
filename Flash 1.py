# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

##Flash 1

#Problema 1

def ProblemaDybala(n):
    i=1
    res=0
    for i in range (0,n+1):
        res=(((-1)**(i+1))*2)/(2*i-1)+res
        i=i+1
        return res
print(ProblemaDybala(1))

#Problema 2

