class Solution(object):
    def groupAnagrams(self, strs):
        
        
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
# the main idea here is that we want to get a list of every word that has the same letters in it
# we use the dictionary because we want to have a key which is the sequence of letters and a value which is the unsorted word #note that sorted() function sorts the word or key into an ascending order and return it as a list so tea would be a e t
# but a list is immutable and cant be considered as a key so we either use a string or tuple as the key
# join() will make the list word into a string and store it as a dictionary key
# as for the value, we need to use the get() method so we can see if the key is there or not and if not the value will be [] as an starting value
# adding to it the unsorted word
# if the key already exists then we will retrieve the current value and add to it the word
# finally we use dictionary.values() method to get the values stored in it as a list

        dic = {}
        for word in strs:
            key = ",".join(sorted(word))
            dic[key] = dic.get(key, []) + [word]
        
        result = dic.values()
        return result
        

        

        