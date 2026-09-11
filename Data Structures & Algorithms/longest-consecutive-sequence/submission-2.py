class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numsSet:
                lenght = 0
                while (n+lenght) in numsSet:
                    lenght+=1
                longest = max(longest, lenght)
        return longest 
        