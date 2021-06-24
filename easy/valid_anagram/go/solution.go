package main

func isAnagram(s string, t string) bool {

	// Solution 1 - Two pass with map for counting letters (2N)
	letter_count := make(map[int]int)

	if len(s) != len(t) {
		return false
	}

	for _, elem := range s {
		letter_count[int(elem)] += 1
	}

	for _, elem := range t {
		if val, ok := letter_count[int(elem)]; ok && val != 0 {
			letter_count[int(elem)] -= 1
		} else {
			return false
		}
	}

	return true

}
