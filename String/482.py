class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        """首先替换掉所有-，并且全部大写，用余数找到一个的长度，然后一直遍历，步长为k,每次叠加进去加一个-符号"""
        s=S.replace("-",'').upper()
        x=len(s)%K
        res=s[:x]
        for i in range(x,len(s),K):
            if res:
                res+='-'+s[i:i+K]
            else:
                res=s[i:i+K]
        return res
