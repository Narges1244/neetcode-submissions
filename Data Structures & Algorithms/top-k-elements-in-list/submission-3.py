class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        result=[]
        for num in nums:
            if num in res:
                res[num]+=1
            else:
                res[num] =1
        ordered = sorted(res, key = lambda x:res[x], reverse=True)
        return ordered[:k]
        