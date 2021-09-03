class Solution:
    def reverse(self, x: int) -> int:
        tmp1=abs(x)
        ans=''
        while(tmp1%10==0 and tmp1!=0):
            tmp1=tmp1//10
        tmp2=str(tmp1)
        del tmp1
        for i in reversed(tmp2):
            ans=ans+i
        if -2**31<=int(ans)<=2**31-1:
            if x<0:
                return -int(ans)
            else:
                return int(ans)
        else:
            return 0
