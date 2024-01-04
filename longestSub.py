class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        my_dict={}
        maximum=0
        i=0
        if (len(s)<1):
            return 0
        for i,char in enumerate(s):
            if char in my_dict and my_dict[char]>=start:
                maximum= max(maximum,i-start)
                start=my_dict[char]+1
            my_dict[char]=i
        maximum= max(maximum,i-start+1)
        return maximum
        



