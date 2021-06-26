package main

type ListNode struct {
    Val int
    Next *ListNode
}
 
func reverseList(head *ListNode) *ListNode {

	// Solution 2 - Iterative
	// if head == nil {
	// 	return nil
	// }

	// if head.Next == nil {
	// 	return head
	// }

	// prev := head
	// curr := head.Next
	// next := curr.Next

	// head.Next = nil

	// for next != nil {
	// 	curr.Next = prev
	// 	prev = curr
	// 	curr = next
	// 	next = next.Next
	// }

	// curr.Next = prev
	// return curr


	// Solution 1 - Recursive
    return reverseListRecursive(nil, head)
}

func reverseListRecursive(prev *ListNode, head *ListNode) *ListNode {
	
	if head == nil {
		return nil
	}

	next := head.Next

	if prev == nil {
		head.Next = nil
	}

	if next == nil {
		head.Next = prev
		return head
	}

	head.Next = prev
	return reverseListRecursive(head, next)
}