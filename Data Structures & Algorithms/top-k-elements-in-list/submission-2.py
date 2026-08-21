class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        arr = [[]for i in range(len(nums)+1)]
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        for num, cnt in count.items():
            arr[cnt].append(num)
        res=[]
        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
            