class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp=-101
        k=0
        for i in range(len(nums)):
            if nums[i]==tmp:
                nums[i]=101
            elif nums[i]>tmp:
                tmp=nums[i]
                k+=1
        nums.sort()
        return k
