class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        mymaximum=nums[-1]
        numbers= [0] * n
        for i in range(len(nums)-2,-1,-1):
            precedent=num[i-1]
            mymaximum=max(nums[i],mymaximum)
            nums[i-1]=mymaximum
        return nums