# singleton element
# input A: a sorted list where only one element in it is unique
# output: the singleton element in the sorted list

import sys

def make_list(fname):
    f = open(fname, "r")
    A = list(f)
    f.close()
    return A


def singleton(A):
    if len(A) == 1:
        return A[0]
    mid = len(A)//2
    if mid%2 == 0: # even
        if A[mid] == A[mid+1]:
            return singleton(A[mid:])
        else:
            return singleton(A[:mid+1])
    else: # odd
        if A[mid] == A[mid+1]: 
            return singleton(A[:mid])
        else:
            return singleton(A[mid+1:]) 


def main():
    A = make_list(sys.argv[1])
    print(singleton(A))


if __name__ == "__main__":
    main()