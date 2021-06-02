class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Solution 1 - Check substrings starting at each index in s, N^2 brute force
        # best_len = 0
        # current_substr = set()
        # start_index = 0

        # i = 0
        # while i < len(s):
        #     letter = s[i]

        #     if letter in current_substr:
        #         if len(current_substr) > best_len:
        #             best_len = len(current_substr)
        #         current_substr.clear()
        #         start_index += 1
        #         i = start_index
        #         letter = s[i]

        #     current_substr.add(letter)
        #     i += 1


        # if len(current_substr) > best_len:
        #     best_len = len(current_substr)
        
        # return best_len


        # Solution 2 - Sliding Window with slices
        best_len = 0
        window = []

        for letter in s:
            if letter in window:
                if len(window) > best_len:
                    best_len = len(window)
                window = window[slice(window.index(letter) + 1, len(window))]
            window.append(letter)

        if len(window) > best_len:
            best_len = len(window)

        return best_len


                
