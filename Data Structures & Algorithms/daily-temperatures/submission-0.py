class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= []
        result = [0]*len(temperatures)
        for i,tem in enumerate(temperatures):
            while stack and tem > stack[-1][0]:
                stackt, stacki = stack.pop()
                result[stacki] = (i-stacki)
            stack.append([tem,i])
        return result

        