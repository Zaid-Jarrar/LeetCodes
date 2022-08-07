class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        
        """

        dic = {}
        length = 0
        for letter in s:    
            if letter not in dic:
                dic[letter]= 1
            else:
                dic.pop(letter) 

        length = len(s) - len(dic)
        if dic:
            length+=1

        return(length)
        