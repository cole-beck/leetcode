from solution import Solution

def test():
    s = Solution()

    act1 = s.fizzBuzz(1)
    exp1 = ["1"]
    print(act1, exp1)
    assert act1 == exp1

    act2 = s.fizzBuzz(3)
    exp2 = ["1","2","Fizz"]
    print(act2, exp2)
    assert act2 == exp2

    act3 = s.fizzBuzz(5)
    exp3 = ["1","2","Fizz","4","Buzz"]
    print(act3, exp3)
    assert act3 == exp3

    act4 = s.fizzBuzz(15)
    exp4 = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    print(act4, exp4)
    assert act4 == exp4

test()