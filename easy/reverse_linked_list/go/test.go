package main

import "fmt"

func main() {
	testSolution()
}


type TestCase struct {
    caseID int
    inputHead *ListNode
	expectedResult *ListNode
}

func testSolution() {

	a5 := ListNode{Val: 6, Next: nil}
	a4 := ListNode{Val: 5, Next: &a5}
	a3 := ListNode{Val: 4, Next: &a4}
	a2 := ListNode{Val: 3, Next: &a3}
	a1 := ListNode{Val: 2, Next: &a2}
	a0 := ListNode{Val: 1, Next: &a1}

	b1 := ListNode{Val: 2, Next: nil}
	b0 := ListNode{Val: 1, Next: &b1}

	c0 := ListNode{Val: 1, Next: nil}

	testCases := []TestCase {
		{caseID: 1, inputHead: &a0, expectedResult: &a3},
		{2, &b0, &b1},
		{3, &c0, &c0},
		{4, nil, nil},
	}
		
	for _, testCase := range testCases {

		fmt.Printf("Test Case %d:\n", testCase.caseID)
		fmt.Printf("Original -> ")
		currNode := testCase.inputHead
		for currNode != nil {
			fmt.Printf("%v ", currNode.Val)
			currNode = currNode.Next
		}

		fmt.Printf("\nReversed -> ")
		currNode = reverseList(testCase.inputHead)
		for currNode != nil {
			fmt.Printf("%v ", currNode.Val)
			currNode = currNode.Next
		}
		fmt.Println("\n")
	}
}