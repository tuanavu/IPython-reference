# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:56:50 2015

@author: tvu
"""

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
m.peek()