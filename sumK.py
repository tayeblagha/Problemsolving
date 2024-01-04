from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_dict = {0: 1}
        
        for i, num in enumerate(nums):
            prefix_sum += num

            # Check if there is a subarray with sum equal to k
            if prefix_sum - k in sum_dict:
                count += sum_dict[prefix_sum - k]
                print(f"Found subarray at indices {sum_dict[prefix_sum - k]} to {i}")

            # Update the sum_dict
            if prefix_sum in sum_dict:
                sum_dict[prefix_sum] += 1
            else:
                sum_dict[prefix_sum] = 1

            print(f"At index {i}, prefix_sum: {prefix_sum}, count: {count}, sum_dict: {sum_dict}")
        
        return count

# Example 1
nums1 = [1, 2, 3, 4, 5]
k1 = 9
sol = Solution()
result1 = sol.subarraySum(nums1, k1)
print(f"Example 1: {result1} subarrays with sum {k1}\n")

# Example 2
nums2 = [3, 4, 7, 2, -3, 1, 4, 2]
k2 = 7
result2 = sol.subarraySum(nums2, k2)
print(f"Example 2: {result2} subarrays with sum {k2}")
