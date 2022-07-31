class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # for index in range(len(t)):
        new_t=list(t)
        for t_char in t:
            
            # s_char = s[index]
            # t_char = t[index]
        
            if t_char not in s :
                new_t.remove(t_char)
            elif t_char in s and s.count(t_char) != new_t.count(t_char):         
                new_t.remove(t_char)
                
        new_t = ''.join(new_t)
        if new_t != s:
            return False
        return True
                
                
        
                
        