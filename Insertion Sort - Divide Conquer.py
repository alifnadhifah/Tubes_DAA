# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:32:56 2020

@author: Alifskiy
"""

def insertionSort(list, n):
    j=0
    print("")
    print("Output Array: ", list[0:1],"(iterasi ke-",j,")")
    for i in range(1,n):
        value = list[i]
        i -= 1
        while i >= 0 :
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i -= 1
                j+=1
                k = j + 1
                print("Output Array: ", list[0:k],"(iterasi ke-",j,")")
            else:
                value = list[i]
                i -= 1
                j+=1
                m = j + 1
                print("Output Array: ", list[0:m],"(iterasi ke-",j,")")

arr = []

k = int(input('Panjang Array: '))

for l in range(k):
    x = int(input('Isi Array: '))
    arr.append(x)
    print("Array: ", arr)

print('')
print("Output Array: ", arr,"(Kondisi Awal Array)")
print('Hasil Divide Conquer: ')
insertionSort(arr, k)

