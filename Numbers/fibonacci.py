#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Thiago Vieira

ub = input('Enter the number of numbers you wanna see: ')
a=0
b=0
c=1
for i in range(0, ub):
	a, b, c = b, c, b+c
	print a
