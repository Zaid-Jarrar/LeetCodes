class Solution(object):
    def isSubsequence(self, s, t):
        
        s_counter = 0
        t_counter=0
        final = ''
        if s == '':
            return True
        elif len(s) < len(t) and s != '' and t != '':

            while s_counter < len(s) and t_counter < len(t):
                
                

                if s[s_counter] == t[t_counter]:
                    
                    final += s[s_counter]
                    s_counter +=1
                    t_counter +=1

                else:
                    
                    t_counter+=1
            if final == s:
                
                return True
            return False

        return False
 

                
        
                
        