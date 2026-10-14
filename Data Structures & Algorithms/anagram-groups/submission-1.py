class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for index, word in enumerate(strs):
            temp = [0] * 26

            for char in word:
                temp[ord(char) - ord('a')] += 1
            
            result[tuple(temp)].append(word)

        return list(result.values())