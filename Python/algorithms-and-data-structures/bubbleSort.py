# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:21:24 2015

@author: tvu
"""

def bubbleSort(myList):
    # bubble sort algorithm
    moreSwaps = True
    while moreSwaps:
        moreSwaps = False
        for element in range(len(myList) - 1):
            if myList[element] > myList[element+1]:
                moreSwaps = True
                myList[element], myList[element+1] = myList[element+1], myList[element]
    return myList

if __name__ == "__main__":
    myList = [5,2,7,1,9,3,6]
    sortedList = bubbleSort(myList)
    print sortedList