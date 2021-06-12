from solution import Solution


class TestCase:
    def __init__(self, case_num, test_string, expected_result):
        self.case_num = case_num
        self.test_string = test_string
        self.expected_result = expected_result


def solution_test():

    solution = Solution()

    test_data = [
        TestCase(1, '', 0),
        TestCase(2, 'z', 1),
        TestCase(3, 'bbbbb', 1),
        TestCase(4, 'pwwkew', 3),
        TestCase(5, 'abbcb', 2),
        TestCase(6, 'abcabcbb', 3),
        TestCase(7, 'abcdefghijklmnopqrstuvwxyz', 26),
        TestCase(8, 'dvdf', 3),
        TestCase(9, 'abcdba', 4)
    ]

    print('Test Case -> Actual Result == Expected Result :: Test String')

    for i in range(len(test_data)):
        case_number = test_data[i].case_num
        actual = solution.lengthOfLongestSubstring(test_data[i].test_string)
        expected = test_data[i].expected_result
        test_string = test_data[i].test_string

        print(f'{case_number} -> {actual} == {expected} :: {test_string}')
        assert (actual == expected), f'Test Case {case_number} failed on string: {test_string}'

solution_test()