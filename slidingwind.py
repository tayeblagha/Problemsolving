def dynamic_sliding_window(arr,target):
    start=0
    current_sum=0
    maximum_sum=0
    for end in range(len(arr)):
        current_sum+=arr[end]
        while current_sum>target and start<len(number):
            current_sum-=arr[start]
            start+=1
        maximum_sum=max(current_sum,maximum_sum)
    return maximum_sum

number=[1,62,3,1,6,4,2,3,61,4,7,15,3,4,8]
print(dynamic_sliding_window(number,20))
