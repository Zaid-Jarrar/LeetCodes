class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = {}
        t_dic = {}
        for letter in s:
            if letter not in s_dic:
                s_dic[letter] = 1
            else:
                s_dic[letter] +=1
        
        for letter in t:
            t_dic[letter] = t_dic.get(letter,0) + 1
        
        if t_dic == s_dic:
            return True
        return False
            
        # OR THIS WAY
        
        # text_s = sorted(s)
        # text_t = sorted(t)
        # if text_s == text_t:
        #     return True
        # return False
        