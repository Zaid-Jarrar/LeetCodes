class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        i = 0
        strs.sort()
        word = strs[0]
        prefix = ''
        while i <= len(strs[0]) :
            prefix = word[:len(word)-i]
            if prefix == strs[-1][:len(prefix)]:          
                return prefix
            i +=1
     
            
            
        