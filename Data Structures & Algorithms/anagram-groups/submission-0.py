class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            letter_count_hashmap = {}
            for char in word:
                letter_count_hashmap[char] = letter_count_hashmap.get(char, 0) + 1
            
                
            key = tuple(sorted(letter_count_hashmap.items()))
            groups.setdefault(key, []).append(word)    
        return list(groups.values())

