# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:00:22 2015

@author: tvu
"""
def binarySearch(myItem,myList):
    found = False
    bottom = 0
    top = len(myList) - 1
    while bottom <= top and not found:
        middle = (bottom + top)//2
        if myList[middle] == myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle - 1
    return found

if __name__ == "__main__":
    numberList = [1,4,6,8,12,15,18,19,24,27,31,42,43,58]
    item = int(raw_input("What number are you looking for? "))
    isitFound = binarySearch(item,numberList)
    if isitFound:
        print("Your number is in the list")
    else:
        print("Your number is not in the list")