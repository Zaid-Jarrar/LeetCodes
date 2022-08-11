import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
# the main idea is to check if the dic of s has the same number of letters as the dic of p but only if their length are             the same

#collections.Counter() helps count the freq of letters in our strings and it is a dic

# index is the sliding index of s starting from 0

# add_index is the sliding index of s starting from the length of p

# we compare between the dic_s and dic_p if they have the same letters and same count as well then we add the starting index to   the result list

# instead of always slicing s towards a new 3 letters moving one index at a time

# we substract  the count of the letter at the index location and if is now counts to 0 then we simply remove it thus   reducing the space

# after that we add from the right side a new letter or we increase the count of an existing letter, depending on the case

# we keep this pattern until the length of add_index is larger than the length of s
# we return the result
        
    
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