class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the middle of array
        start , end = 0, len(nums)-1
        
        while start <= end:
            middle = (start + end )//2
            if  target < nums[middle]:
                end = middle -1
            elif target > nums[middle]:
                start = middle +1
            elif target == nums[middle]:
                return middle
        return -1




        # check if middle is greater or less than target
        #choose which part of array we should search
        