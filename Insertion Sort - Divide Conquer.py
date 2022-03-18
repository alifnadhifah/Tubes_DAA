# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:32:56 2020

@author: Alifskiy
"""

#function insertion sort algorithm ascending
def insertionSort1(list, n):
    print("")
    print("Output Array: ", list, '(iterasi ke-0)')
    #Algoritma Utama Insertion Sort ascending
    for i in range(1,n):
        value = list[i]
        j = i - 1
        #Algoritma Utama Divide & Conquer
        while j>= 0 and list[j] > value:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = value
        print("Output Array: ", list, '(iterasi ke-',i,')')

def insertionSort2(list, n):
    print("")
    print("Output Array: ", list, '(iterasi ke-0)')
    #Algoritma Utama Insertion Sort descending
    for i in range(1,n):
        value = list[i]
        j = i - 1
        #Algoritma Utama Divide & Conquer
        while j>= 0 and list[j] < value:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = value
        print("Output Array: ", list, '(iterasi ke-',i,')')

#start program with initialization and variable assignment
arr = []

k = int(input('Panjang Array: '))

for l in range(k):
    x = int(input(f'Isi Array ke-{l}: '))
    arr.append(x)

#print variable value
print('')
print("Output Array: ", arr,"(Kondisi Awal Array)")
print('')
print('Hasil Divide Conquer: ')
ascordesc = str(input('Urutkan Secara Ascending/Descending(asc/desc): '))
if (ascordesc=='asc'):
    print('Hasil Divide Conquer: ')
    insertionSort1(arr, k)
    print('Pengurutan secara Ascending Selesai :)')
elif (ascordesc=='desc'):
    print('Hasil Divide Conquer: ')
    insertionSort2(arr, k)
    print('Pengurutan secara Descending Selesai :)')
