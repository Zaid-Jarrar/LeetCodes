class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        text_s = ','.join((sorted(s)))
        text_t = ','.join((sorted(t)))
        if text_s == text_t:
            return True
        return False
        