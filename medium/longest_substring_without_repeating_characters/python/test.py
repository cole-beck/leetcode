from solution import Solution


class TestCase:
    def __init__(self, case_num, input_string, expected_result):
        self.case_num = case_num
        self.input_string = input_string
        self.expected_result = expected_result


def solution_test():

    solution = Solution()

    test_cases = [
        TestCase(1, '', 0),
        TestCase(2, 'z', 1),
        TestCase(3, 'bbbbb', 1),
        TestCase(4, 'pwwkew', 3),
        TestCase(5, 'abbcb', 2),
        TestCase(6, 'abcabcbb', 3),
        TestCase(7, 'abcdefghijklmnopqrstuvwxyz', 26),
        TestCase(8, 'dvdf', 3),
        TestCase(9, 'abcdba', 4),
        TestCase(10, 'vvvedevevvv', 3)
    ]

    print('Test Case -> Actual Result == Expected Result')
    for case in test_cases:
        actual = solution.lengthOfLongestSubstring(case.input_string)
        expected = case.expected_result

        print(f'{case.case_num} -> {actual} == {expected}')
        assert (actual == expected), f'Test Case {case.case_num} failed on string: {case.input_string}'

solution_test()