class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        d = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] +=1
        
        for letter in t:
            d[letter] = d.get(letter,0) + 1
        
        if d == dic:
            return True
        return False
            
        # OR THIS WAY
        
        # text_s = sorted(s)
        # text_t = sorted(t)
        # if text_s == text_t:
        #     return True
        # return False
        