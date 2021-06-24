package main

import "fmt"

func main() {
	testSolution()
}


type TestCase struct {
    caseID int
    inputSlice []int
	inputTarget int
	expectedResult []int
}

func testSolution() {

	testCases := []TestCase {
		{caseID: 1, inputSlice: []int{1,1}, inputTarget: 2, expectedResult: []int{0,1}},
		{2, []int{2,7,11,15}, 18, []int{1,2}},
		{3, []int{2,7,11,6,1,0}, 7, []int{3,4}},
		{4, []int{2,7,11,6,1,0}, 50, []int{0,0}},
		{5, []int{1000,3,2,1}, 1001, []int{0,3}},
		{6, []int{3,2,8,4,1,3,6,10,58,1}, 2, []int{4,9}},
	}
	
	fmt.Println("Test Case -> Actual Result == Expected Result")
	
	for _, testCase := range testCases {

		actualResult := twoSum(testCase.inputSlice, testCase.inputTarget)

		fmt.Printf("%d -> %v == %v\n", testCase.caseID, actualResult, testCase.expectedResult)
		if !compareResults(actualResult, testCase.expectedResult) {
			fmt.Printf("Test Case %d: Failed with input slice %v and input target %d\n", 
				testCase.caseID, testCase.inputSlice, testCase.inputTarget)
		} 
	}
}

func compareResults(a, b []int) bool {

	for i, val := range a {
		if val != b[i] {
			return false
		}
	}

	return true
}