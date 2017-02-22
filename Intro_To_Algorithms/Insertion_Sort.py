#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def Insertion_Sort(arr):
	len_arr = len(arr)
	for i in range(1,len_arr):
		key = arr[i]
		j =  i - 1
		while j >= 0 and key < arr[j] :
			arr[j+1] = arr [j]
			j = j -1
		arr[j+1] = key 

	return arr

def main():
	arr = []
	for i in range(0,100):
		arr.append(random.randint(0,100))
	print(arr)
	print(Insertion_Sort(arr))
	print(arr)

if __name__ == '__main__':
	main()
