class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_num = str(x)
        if string_num == string_num[::-1]:
            return True
        return False

        