package main

import "fmt"

func main() {
	testSolution()
}


type TestCase struct {
	caseID int
	input []int
}

func testSolution() {

	testCases := []TestCase {
		{caseID: 1, input: []int{}},
		{2, []int{0}},
		{3, []int{1, 0}},
		{4, []int{0, 1, 1}},
		{5, []int{3, -2, -1}},
		{6, []int{-1, 0, 1, 2, -1, -4}},
		{7, []int{0, 0, 0, 0}},
		{8, []int{-2, 0, 0, 2, 2}},
	}

	fmt.Println("Test Case ID -> Result")

	for _, testCase := range testCases {
		
		result := threeSum(testCase.input)

		fmt.Printf("%d -> %v\n", testCase.caseID, result)
	}
}