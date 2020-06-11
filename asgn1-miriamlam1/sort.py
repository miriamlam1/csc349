import sys
import time

# A : unsorted list

# Selection Sort
# repeatedly selects the smallest element from the unsorted elements
def selection_sort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i+1, len(A)):
            if A[j] < A[mini]:
                mini = j
        A[mini], A[i] = A[i], A[mini]

# Insertion Sort
# repeatedly inserts the next unsorted element into a sorted section
def insertion_sort(A):
    for i in range(1, len(A)):
        curr = A[i]
        j = i
        while j > 0 and A[j-1] > curr:
            A[j] = A[j-1]
            j-=1
        A[j] = curr


# Merge Sort
# recursively sorts the two halves of a sequence,
# then merges the sorted halves back together
def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        merge_sort(L) # left
        merge_sort(R) # right
        i = j = k = 0 # i = L index j = R index k = A index
        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1
            k+=1
        while i < len(L):
            A[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            A[k]=R[j]
            j+=1
            k+=1

def make_list(fname):
    A = (open(fname)).read()
    A = A.strip()
    A = A.split(", ")
    A = [int(i) for i in A]
    return A

def main():
    A = make_list(sys.argv[1])
    time1 = time.time()
    selection_sort(A)
    time2 = time.time()
    print("Selection Sort", "({:.2f}".format((time2-time1)*1000), "ms):", str(A)[1:-1])

    A = make_list(sys.argv[1])
    time1 = time.time()
    insertion_sort(A)
    time2 = time.time()
    print("Insertion Sort", "({:.2f}".format((time2-time1)*1000), "ms):", str(A)[1:-1])

    
    A = make_list(sys.argv[1])
    time1 = time.time()
    merge_sort(A)
    time2 = time.time()
    print("Merge Sort    ", "({:.2f}".format((time2-time1)*1000), "ms):", str(A)[1:-1])


if __name__ == "__main__":
    main()