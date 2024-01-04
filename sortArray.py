class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lastNums2=0
        i=0
        while i<len(nums1):
            item=nums1[i]
            if item > nums2[lastNums2]:
                nums1.insert(i,nums2[lastNums2])
                lastNums2+=1
            i+=1
        
        if lastNums2!=len(nums2)-1:
            nums1.append(nums2[lastNums2:])
 

# numbers= [1,2,6,9,5,8]
# numbers.insert(2,3)
# print(numbers)

        