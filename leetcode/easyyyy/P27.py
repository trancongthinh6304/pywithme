class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i-k]==val:
                nums.pop(i-k)
                k+=1
        return len(nums)