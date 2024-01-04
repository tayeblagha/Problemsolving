def insertSort0(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr


numbers=[1,6,9,3,-2,69,1,0,3]

def insert(n, arr):
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
        print(*arr)

insert(5, [4, 1, 5, 9, 3])

