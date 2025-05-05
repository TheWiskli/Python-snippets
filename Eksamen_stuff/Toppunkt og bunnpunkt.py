# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:27:00 2022

@author: paland620
"""

def f(x):
    return -x**2-4*x+2

x = -5
dx = 1E-4

while f(x) < f(x+dx): # toppunkt f(x) <..., bunnpunkt f(x) >.... 
    x = x + dx


x = round(x,3)
print(x)
print("ferdig")
