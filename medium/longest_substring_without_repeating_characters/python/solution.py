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
        # best_len = 0
        # window = []

        # for letter in s:
        #     if letter in window:
        #         if len(window) > best_len:
        #             best_len = len(window)
        #         window = window[slice(window.index(letter) + 1, len(window))]
        #     window.append(letter)

        # if len(window) > best_len:
        #     best_len = len(window)

        # return best_len


        # Solution 3 - Sliding window with dict to track last letter indices
        letter_idx_dict = {}
        start_ptr = 0
        end_ptr = 0
        max_len = 0

        for end_ptr in range(len(s)):
            letter = s[end_ptr]

            if letter in letter_idx_dict:
                start_ptr = max(start_ptr, letter_idx_dict[letter] + 1)
            max_len = max(max_len, end_ptr - start_ptr + 1)
            letter_idx_dict[letter] = end_ptr

        return max_len