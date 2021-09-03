class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(1,len(nums)+1):
            x=nums[0]
            y=target-nums[0]
            nums.pop(0)
            if y in nums:
                ans.append(i-1)
                ans.append(nums.index(y)+i)
                break
        return ans
