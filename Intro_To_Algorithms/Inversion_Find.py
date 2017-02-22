#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 归并排序修改逆序对查找 算法
# 即 统计归并时，非正常序次数，用num_count来记数

global num_count

num_count = 0 

def merge(arr1,arr2):
	global num_count
	len_arr1 = len(arr1)
	i_arr1 = 0
	len_arr2 = len(arr2)
	i_arr2 = 0
	arr = []
	while i_arr1 <= len_arr1  and i_arr2 <= len_arr2 :
		if i_arr1 == len_arr1 :
			arr.extend(arr2[i_arr2:len_arr2]) #arr1没有对时候，将arr2剩余 添加到末尾
			break
		if i_arr2 == len_arr2:
			arr.extend(arr1[i_arr1:len_arr1]) #arr2 没有对象时，将arr1剩余 添加到末尾
			num_count = num_count + (len_arr1 - i_arr1 -1)* len_arr2 
			break
		if arr1[i_arr1] <= arr2[i_arr2]:
			arr.append(arr1[i_arr1])
			i_arr1 = i_arr1 + 1;
		else :
			arr.append(arr2[i_arr2])
			i_arr2 = i_arr2 + 1;
			num_count = num_count + (len_arr1 - i_arr1)
	
	return arr

def merge_sort(arr):
	len_arr = len(arr)

	if len_arr == 1 :
		return arr
	elif len_arr == 0:
		return []
	else:
		return merge(merge_sort(arr[0:int(len_arr/2)]),merge_sort(arr[int(len_arr/2):len_arr]))

def main():
	global num_count
	arr = [2,3,8,6,1]
	print(merge_sort(arr))
	print(num_count)


if __name__ == '__main__':
	main()