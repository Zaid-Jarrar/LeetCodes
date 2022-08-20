class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # i = 0
        # prefix = strs[0]
        # while i <= len(strs[0]):
        #     if prefix == strs[-1][:len(prefix)]:
        #         print(prefix)
        #         return prefix
        #     i +=1
        #     prefix = strs[0][:len(prefix)-i]
        i = 0
        strs.sort()
        word = strs[0]
        prefix = ''
        while i <= len(strs[0]) :
            prefix = word[:len(word)-i]
            # print(i,prefix,strs[-1][:len(prefix)])
            if prefix == strs[-1][:len(prefix)]:
                # print('yes')
          
                return prefix
            i +=1
            # return ''     
            
            
        