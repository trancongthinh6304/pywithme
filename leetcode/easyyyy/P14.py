class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_strs=[]
        k=0
        for i in range(len(strs)):
            len_strs.append(len(strs[i]))
        for i in range(min(len_strs)):
            tmp=strs[0][i]
            ok=True
            for j in range(len(strs)):
                if strs[j][i]!=tmp:
                    ok=False
                    break
            if not ok:
                break
            else:
                k+=1
        if k>0:
            return strs[0][0:k]
        else:
            return ""
