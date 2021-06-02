from solution import Solution

def test():
    s = Solution()

    act1 = s.lengthOfLongestSubstring('')
    exp1 = 0
    print(act1, exp1)
    assert act1 == exp1

    act2 = s.lengthOfLongestSubstring('z')
    exp2 = 1
    print(act2, exp2)
    assert act2 == exp2

    act3 = s.lengthOfLongestSubstring('bbbbb')
    exp3 = 1
    print(act3, exp3)
    assert act3 == exp3

    act4 = s.lengthOfLongestSubstring('pwwkew')
    exp4 = 3
    print(act4, exp4)
    assert act4 == exp4

    act5 = s.lengthOfLongestSubstring('abbcb')
    exp5 = 2
    print(act5, exp5)
    assert act5 == exp5

    act6 = s.lengthOfLongestSubstring('abcabcbb')
    exp6 = 3
    print(act6, exp6)
    assert act6 == exp6

    act7 = s.lengthOfLongestSubstring('abcdefghijklmnopqrstuvwxyz')
    exp7 = 26
    print(act7, exp7)
    assert act7 == exp7

    act8 = s.lengthOfLongestSubstring('dvdf')
    exp8 = 3
    print(act8, exp8)
    assert act8 == exp8

test()