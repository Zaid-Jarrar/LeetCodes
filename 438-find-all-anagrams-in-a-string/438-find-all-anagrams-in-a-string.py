import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        
        dic_s = collections.Counter(s[:len(p)])
        dic_p = collections.Counter(p)
        result = []
        
        index = 0
        add_index = len(p)
        
        while add_index <= len(s):
            if dic_s == dic_p:
                result.append(index)
            
            dic_s[s[index]] -= 1
            if dic_s[s[index]] == 0:
                dic_s.pop(s[index])
            
            if add_index < len(s):
                dic_s[s[add_index]] +=1
                
            index +=1
            add_index +=1
        return result
                    
        
        # OR THIS BUT IT IS Alot SLOWER and thus fails the time allowed 
#         result = []
        
#         for index in range(len(s)):  
            
#             s_cut = s[index:len(p)+index]
#             # if counter(s_cut) == counter(p):
#             if sorted(s_cut) == sorted(p):
#                 result.append(index)
#         return result
          
                    

# def counter(text):
#     dic={}
#     for letter in text:
#         dic[letter] = dic.get(letter,0) + 1
#     return dic