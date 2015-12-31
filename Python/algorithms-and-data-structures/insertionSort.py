# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:32:29 2015

@author: tvu
"""

def insertionSort(data):
    data_size = len(data)
    current = 1
    while current < data_size:
        for i in range(current):
            if data[current] < data[i]:
                temp = data[i]
                data[i] = data[current]
                data[current] = temp

        current += 1

    return data

if __name__ == "__main__":
    myList = [5,2,7,1,9,3,6]
    sortedList = insertionSort(myList)
    print sortedList