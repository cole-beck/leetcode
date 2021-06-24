class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Solution 1 - Dictionary with letter count (2N)
        letter_count = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        for letter in t:
            if letter in letter_count and letter_count[letter] is not 0:
                letter_count[letter] -= 1
            else:
                return False
        
        return True