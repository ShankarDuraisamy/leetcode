from typing import List


class FirstOccurrence:
	@staticmethod
	def solve(haystack: str, needle: str):
		left_ptr = 0
		check_ptr = left_ptr
		needle_ptr = 0
		while check_ptr < len(haystack) and needle_ptr < len(needle):
			if haystack[check_ptr] == needle[needle_ptr]:
				check_ptr += 1
				needle_ptr += 1
			else:
				left_ptr += 1
				check_ptr = left_ptr
				needle_ptr = 0
			if needle_ptr == len(needle) -1:
				return left_ptr
		return -1

	@staticmethod
	def solve1(haystack: str, needle: str):
		left_ptr = 0
		while left_ptr < len(haystack) - len(needle) + 1:
			if haystack[left_ptr: left_ptr + len(needle)] == needle:
				return left_ptr
			else:
				left_ptr += 1
		return -1


if __name__ == "__main__":
	haystack = "a"
	needle = "a"
	print(FirstOccurrence.solve1(haystack, needle))
