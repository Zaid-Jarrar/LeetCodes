class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # main idea here is get rid of the edge cases but replacing them with what can be taken from the dic and then summing them all together 
        
        result = 0
        dic = {
            "I":  1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
       
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")
        
        for rom in s:
            result += dic[rom]
        return result
            

                
            
        