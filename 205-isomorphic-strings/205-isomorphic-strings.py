class Solution(object):
    def isIsomorphic(self, s, t):
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = 0
        len_t = 0
        for char in s:
            len_s +=1
        
        for char in t:
            len_t +=1  
            
        if len_s != len_t:
            return False
        
        char_storage = {}
        
        mapped = set()
        for index in range(len_s):
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
                
                
        