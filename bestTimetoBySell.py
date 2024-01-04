mapping= {"1":5,"2":7,"5":3}
print(min(mapping.keys()))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        currect_ammout=0
        mapping={}
        mapping[prices[0]]=0
        for i in range(1,len(prices)):
            currect_ammout=prices[i]-min(mapping.keys())
            maximum=max(maximum,currect_ammout)
            mapping[prices[i]]=i

            
