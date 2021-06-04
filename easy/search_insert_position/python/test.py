from solution import Solution

def test():
    s = Solution()

    act1 = s.searchInsert([1, 2, 3], 2)
    exp1 = 1 
    print(act1, exp1)
    assert act1 == exp1

    act2 = s.searchInsert([1, 2, 3], 4)
    exp2 = 3
    print(act2, exp2)
    assert act2 == exp2

    act3 = s.searchInsert([1, 2, 3], -1)
    exp3 = 0
    print(act3, exp3)
    assert act3 == exp3

    act4 = s.searchInsert([2, 4, 6, 8, 10, 12, 4000], 4000)
    exp4 = 6
    print(act4, exp4)
    assert act4 == exp4

    act5 = s.searchInsert([2, 4, 6, 8, 10, 12, 5000], 11)
    exp5 = 5
    print(act5, exp5)
    assert act5 == exp5

    act6 = s.searchInsert([2, 4, 6, 8, 10, 12, 5000], 4999)
    exp6 = 6
    print(act6, exp6)
    assert act6 == exp6

    act7 = s.searchInsert([1, 3], 0)
    exp7 = 0
    print(act7, exp7)
    assert act7 == exp7

test()