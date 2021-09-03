class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        romans={'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 
                'M': 1000}
        i=0
        while(i<len(s)):
            if i+1>=len(s):
                num=num+romans[s[i]]
                i+=1
            else:
                if s[i]=='I':
                    if s[i+1]=='V' or s[i+1]=='X':
                        num=num+romans[s[i+1]]-1
                        i+=2
                    else:
                        num=num+romans[s[i]]
                        i+=1
                elif s[i]=='X':
                    if s[i+1]=='L' or s[i+1]=='C':
                        num=num+romans[s[i+1]]-10
                        i+=2
                    else:
                        num=num+romans[s[i]]
                        i+=1
                elif s[i]=='C':
                    if s[i+1]=='D' or s[i+1]=='M':
                        num=num+romans[s[i+1]]-100
                        i+=2
                    else:
                        num=num+romans[s[i]]
                        i+=1
                else: 
                    num=num+romans[s[i]]
                    i+=1
        return num
