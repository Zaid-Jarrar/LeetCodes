class Solution(object):
    def isIsomorphic(self, s, t):
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
 

        if len(s) != len(t):
            return False
        
        char_storage = {}
        
        mapped = set()
        for index in range(len(s)):
            s_char = s[index]
            t_char = t[index]
            if s_char in char_storage:
                if char_storage[s_char] != t_char:
                    return False
            else:
                if t_char in mapped:
                    return False
            
            char_storage[s_char] = t_char
            mapped.add(t_char)
        
        return True
                
                
        