class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        ans=''
        for i in reversed(x):
            ans+=i
        return x==ans
