package main

import "fmt"

func main() {
	testSolution()
}


type TestCase struct {
	caseID int
	input1 string
	input2 string
	expectedResult bool
}

func testSolution() {

	testCases := []TestCase {
		{caseID: 1, input1: "a", input2: "a", expectedResult: true},
		{2, "b", "bc", false},
		{3, "dog", "god", true},
		{4, "banana", "ananab", true},
		{5, "orange", "apple", false},
	}

	fmt.Println("Test Case -> Actual Result == Expected Result")

	for _, testCase := range testCases {
		
		actualResult := isAnagram(testCase.input1, testCase.input2)

		fmt.Printf("%d -> %v == %v\n", testCase.caseID, actualResult, testCase.expectedResult)
		if actualResult != testCase.expectedResult {
			fmt.Printf("Test Case %d: Failed with input strings %s and %s\n", 
				testCase.caseID, testCase.input1, testCase.input2)
		} 
	}
}