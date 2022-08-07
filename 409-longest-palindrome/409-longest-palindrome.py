class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        # the main idea here is that we want to find the letters that only appeared once and place them in a dic or a set
        # because then we can substract the length of the whole string by the length of the dic or set 
        # we would only add 1 if the dic is not empty because logically only 1 single char of the dic can exist in the palindrome string
        
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
        