#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##寻找最大子数组

def find_max_crossing_subarray(a,low,mid,high):
	leftsum = - float("inf")
	sum = 0 
	for i in range(mid,low-1,-1):
		sum = sum + a[i]
		if sum > leftsum :
			leftsum = sum
			maxleft = i

	rightsum = - float("inf")
	sum = 0
	for j in range(mid+1,high+1,1):
		sum = sum + a[j]
		if sum >  rightsum :
			rightsum = sum
			maxright = j

	return maxleft, maxright,leftsum+rightsum

def find_maximum_subarray(a,low,high):
	if high == low :
		return low, high, a[low]
	else :
		mid = int((low+high)/2)
		leftlow, lefthigh, leftsum = find_maximum_subarray(a, low, mid)
		rightlow, righthigh, rightsum = find_maximum_subarray(a, mid+1, high)
		crosslow, crosshigh, crosssum = find_max_crossing_subarray(a, low, mid, high)
		if leftsum >= rightsum and  leftsum >= crosssum :
			return leftlow, lefthigh, leftsum
		elif rightsum >= leftsum and rightsum >= crosssum :
			return rightlow, righthigh, rightsum
		else :
			return crosslow, crosshigh, crosssum

def main():
	a = [1,2,3,4,5,-6,-7,8,9,-10,2,3,4,-1,-4,1]
	low = 0 
	high = len(a) - 1
	print(find_maximum_subarray(a,low,high))

if __name__ == '__main__':
	main()


