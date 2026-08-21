class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_nums = {}
        for i, n in enumerate(nums):
            all_nums[n] = i
        for i,n in enumerate (nums):
            diff = target - n
            if diff in all_nums and all_nums[diff] != i:
                return [i, all_nums[diff]]
        return []