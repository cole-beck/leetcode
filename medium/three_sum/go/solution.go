package main

import "sort"


func threeSum(nums []int) [][]int {
	
	// Solution 2 - Sort and convert to n sorted two sum subproblems (n^2)
	var output [][]int
	sort.Ints(nums)

	for i := 0; i < len(nums); i++ {
		if i != 0 && nums[i] == nums[i - 1] { continue }
		target := -1 * nums[i]
		start := i + 1
		end := len(nums) - 1
		for start < end {
			if start - 1 != i && nums[start - 1] == nums[start] || nums[start] + nums[end] < target { 
				start++
			} else if nums[start] + nums[end] > target {
				end--
			} else {
				output = append(output, []int{nums[i], nums[start], nums[end]})
				start++
				end--
			}

		}
	}

	return output


	// Solution 1 - Brute force: A truly awful solution that doesn't even work (N^3)
	// var sol [][]int

	// for i := 0; i < len(nums) - 2; i++ {
	// 	for j := i + 1; j < len(nums) - 1; j++ {
	// 		for k := j + 1; k < len(nums); k++ {
	// 			if nums[i] + nums[j] + nums[k] == 0 {
	// 				triplet := []int{nums[i], nums[j], nums[k]}
	// 				sol = append(sol, triplet)
	// 			}
	// 		}
	// 	}
	// }

	// var sliceDupes []int

	// for i := 0; i < len(sol) - 1; i++ {
	// 	for j := i + 1; j < len(sol); j++ {
	// 		dupCount := 0
	// 		for k := 0; k < 3; k++ {
	// 			for l := 0; l < 3; l++ {
	// 				if sol[i][k] == sol[j][l] {
	// 					dupCount++
	// 					if dupCount == 3 {
	// 						sliceDupes = append(sliceDupes, j)
	// 					}
	// 				}
	// 			}
	// 		}
	// 		dupCount = 0
	// 	}
	// }

	// for _, dupe_idx := range sliceDupes {
	// 	firstHalf := sol[:dupe_idx]
	// 	lastHalf := sol[dupe_idx + 1:]
	// 	sol = firstHalf
	// 	for _, slice := range lastHalf {
	// 		sol = append(sol, slice)
	// 	}
	// }

	// return sol

}