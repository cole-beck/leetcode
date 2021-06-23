package main

func twoSum(nums []int, target int) []int {
	
	// Solution 2 - One pass with Map (N)
	index_map := make(map[int]int)

	for i, element := range nums {
		if _, ok := index_map[target - element]; ok {
			return []int{index_map[target - element], i}
		} else {
			index_map[element] = i
		}
	}

	return []int{0, 0}


	// Solution 1 - Brute Force (N^2)
	// var solution []int

	// for i := 0; i < len(nums) - 1; i++ {
	// 	for j := i + 1; j < len(nums); j++ {
	// 		if nums[i] + nums[j] == target {
	// 			solution = append(solution, i, j)
	// 		}
	// 	}
	// }

	// return solution
}