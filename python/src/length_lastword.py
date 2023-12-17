from typing import List


class LastWordLength:

	@staticmethod
	def solve(s: str) -> bool:
		right_ptr = len(s) - 1
		while s[right_ptr] == ' ':
			right_ptr -= 1
		count_ptr = right_ptr
		while s[right_ptr] != ' ':
			right_ptr -= 1
		return count_ptr - right_ptr


if __name__ == "__main__":
	print(LastWordLength.solve("anagram test wwer  eeee     "))
