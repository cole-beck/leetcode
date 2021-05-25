from solution import twoSum

def test():
    act1 = twoSum([1, 2, 3], 5)
    exp1 = [1, 2] 
    print(act1, exp1)
    assert act1 == exp1

    act2 = twoSum([3, 3], 6)
    exp2 = [0, 1]
    print(act2, exp2)
    assert act2 == exp2

    act3 = twoSum([1000, 3, 2, 1], 1001)
    exp3 = [0, 3]
    print(act3, exp3)
    assert act3 == exp3

    act4 = twoSum([3, 2, 8, 4, 1, 3, 6, 10, 58, 1], 2)
    exp4 = [4, 9]
    print(act4, exp4)
    assert act4 == exp4

test()