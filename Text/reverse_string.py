#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Thiago Vieira

def reverse(text):
	reverse_str=""
	for i in range(len(text)-1, -1, -1):
		reverse_str += text[i]
	return reverse_str

def another_reverse(text):
	return text[::-1]

text = raw_input()
print "Reverse: " + reverse(text)
print "Another reverse: " + another_reverse(text)
