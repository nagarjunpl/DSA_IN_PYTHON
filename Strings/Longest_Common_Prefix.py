class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Compare prefix with each word in the list (starting from the 2nd string)
        for word in strs[1:]:
            # Keep reducing the prefix until it matches the start of 'word'
            while word.find(prefix) != 0:
                # Remove the last character from prefix
                prefix = prefix[:-1]
                
                # If prefix becomes empty, no common prefix exists
                if not prefix:
                    return ""
        
        # Return the longest common prefix found
        return prefix
