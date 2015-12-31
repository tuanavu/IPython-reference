# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:27:16 2015

@author: tvu
"""

def linearSearch(myItem,myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position += 1
    return found

if __name__ == "__main__":
    shopping = ["apples","bananas","chocolate","pasta"]
    item = raw_input("What item do you want to find? ")
    isitFound = linearSearch(item,shopping)
    if isitFound:
        print("Your item is in the list")
    else:
        print("Your item is not in the list")
    
    