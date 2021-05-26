from solution import maxProfit

def test():
    act1 = maxProfit([7,1,5,3,6,4])
    exp1 = 5
    print(act1, exp1)
    assert act1 == exp1

    act2 = maxProfit([7,6,5,4])
    exp2 = 0
    print(act2, exp2)
    assert act2 == exp2

    act3 = maxProfit([1])
    exp3 = 0
    print(act3, exp3)
    assert act3 == exp3

    act4 = maxProfit([3, 2, 8, 4, 0, 3, 6, 10, 5800, 1])
    exp4 = 5800
    print(act4, exp4)
    assert act4 == exp4

    act5 = maxProfit([0, 2])
    exp5 = 2
    print(act5, exp5)
    assert act5 == exp5

test()