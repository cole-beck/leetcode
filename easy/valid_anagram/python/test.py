from solution import Solution


class TestCase:
    def __init__(self, case_id, input_1, input_2, expected_result):
        self.case_id = case_id
        self.input_1 = input_1
        self.input_2 = input_2
        self.expected_result = expected_result


def solution_test():

    solution = Solution()

    test_cases = [
        TestCase(1, "a", "a", True),
        TestCase(2, "b", "bc", False),
        TestCase(3, "dog", "god", True),
        TestCase(4, "banana", "ananab", True),
        TestCase(5, "orange", "apple", False),
    ]

    print('Test Case -> Actual Result == Expected Result')
    for case in test_cases:
        actual = solution.isAnagram(case.input_1, case.input_2)
        expected = case.expected_result

        print(f'{case.case_id} -> {actual} == {expected}')
        assert (actual == expected), \
            f'Test Case {case.case_id} failed on strings: {case.input_1} and {case.input_2}'


if __name__ == "__main__":
    solution_test()