import math
import numpy as np
import sys

class Nut:
    def __init__(self,idx, s):
        self.index = idx
        self.size = s

def partition(nut_array, bolt_pivot,left,right):
    i = left
    flag = -1
    for k in range(left,right+1):
        if nut_array[k].size == bolt_pivot:
            flag = k #find pivot
            print 'pivot {} founded'.format(bolt_pivot)
    if flag >= 0:
        nut_array[flag], nut_array[right] = nut_array[right], nut_array[flag]#swap pivot to front
        for j in range(left,right):
            if nut_array[j].size >= bolt_pivot:
                nut_array[j], nut_array[i] = nut_array[i], nut_array[j]
                i = i+1
        nut_array[i], nut_array[right] = nut_array[right], nut_array[i]
        return i
    return -1


def q_select(bolt_array,nut_array,left,right,k):
    if left == right:
        print 'eureka!'
        return nut_array[left]
    bolt_idx = np.random.randint(0,len(bolt_array))#pick a pivot bolt randomly
    bolt_array[bolt_idx],bolt_array[-1] = bolt_array[-1],bolt_array[bolt_idx]
    print "current_pivot: ",bolt_array[-1]
    pivot_pos = partition(nut_array,bolt_array[-1],left,right)
    print "current_nuts: ", [nut.size for nut in nut_array]
    print "pivot_pos: ", pivot_pos
    if pivot_pos != -1:
        bolt_array.pop(-1)
    if pivot_pos == k-1:
        print 'eureka!'
        return nut_array[pivot_pos]
    elif pivot_pos < k-1:
        return q_select(bolt_array,nut_array,pivot_pos+1,right,k)
    elif pivot_pos > k-1:
        return q_select(bolt_array,nut_array,left,pivot_pos-1,k)
    else:
        return q_select(bolt_array,nut_array,left,right,k)#pick another random nut and do the test again


argv=[[5,4,1,7,6,0,3,2],1]
#create a nut array
print argv
size_array = argv[0]
nuts = [Nut(i,s) for i,s in zip(range(0,len(size_array)), size_array)]
bolts = range(len(nuts))
print [(nut.index,nut.size) for nut in nuts], bolts
k_largest = q_select(bolts,nuts,0,len(nuts)-1,argv[1])
print k_largest.index 
    
