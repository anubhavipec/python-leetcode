from typing import List
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res:List[List[int]] = []
        
        def dfs(i,curr,target):
            # print(curr)
            if sum(curr) == target:
                res.append(curr.copy())
                return
            elif sum(curr) > target or i >= len(nums):
                return
            curr.append(nums[i])
            
            dfs(i,curr,target)
            curr.pop()
            dfs(i+1,curr,target)
        dfs(0,[],target)
        # print(f"res is {res}")
        return res
            
nums=[2,5,6,9]
target=9
            
sol = Solution()
sol.combinationSum(nums,target)