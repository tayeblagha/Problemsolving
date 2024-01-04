class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping_sum= {}
        my_index=[]
        for i in range(len(nums)):
            if (target-nums[i]) in mapping_sum:
                my_index=[i,mapping_sum[target-nums[i]]]
                break
            else:
                mapping_sum[nums[i]]=i
        return my_index        
