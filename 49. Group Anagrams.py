class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        hash = {}
        for element in strs:
            k = ''.join(sorted(list(element)))
            if k in hash:
                hash[k].append(element)
            else:
                hash[k] = [element]
        return(hash.values())