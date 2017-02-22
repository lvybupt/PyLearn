#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#冒泡排序算法

import random

def bubble_sort(arr):
	len_arr = len(arr)
	for i in range(0, len_arr-2):
		for j in range(len_arr-1, i, -1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
	return arr




def main():
	arr = []
	for i in range(0,100):
		arr.append(random.randint(0,100))
	print(arr)
	print(bubble_sort(arr))
	#print(arr)

if __name__ == '__main__':
	main()