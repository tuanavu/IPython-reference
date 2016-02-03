# -*- coding: utf-8 -*-
"""
Created on Fri Jan 01 20:17:09 2016

@author: tvu
"""

# Capitalize!
# https://www.hackerrank.com/contests/pythonist3/challenges/capitalize/copy-from/4436964
"""
Problem Statement

You are given a string S. Your task is to capitalize each word of S.

Input Format

A single line of input containing the string, S.

Constraints

0<len(S)<1000
The string consists of alphanumeric characters and spaces.

Output Format

Print the capitalized string, S.

Sample Input

hello world

Sample Output

Hello World
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

word_re = re.compile("\w+")
def _cap(match):
    return match.group(0).capitalize()

def capitalize_all():
    line = raw_input("")
    return word_re.sub(_cap, line)

print(capitalize_all())