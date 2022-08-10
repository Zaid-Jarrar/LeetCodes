class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        text_s = sorted(s)
        text_t = sorted(t)
        if text_s == text_t:
            return True
        return False
        