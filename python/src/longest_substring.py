from typing import List


class LengthOfLongestSubString:
	@staticmethod
	def solve(s: str) -> int:
		hash_table = {}
		count = 0
		right_ptr = 0
		left_ptr = 0
		result = 0
		while right_ptr < len(s):
			if s[right_ptr] in hash_table:
				result = len(hash_table) if result < len(hash_table) else result
				while s[left_ptr] != s[right_ptr]:
					del hash_table[s[left_ptr]]
					left_ptr += 1
				left_ptr += 1
			else:
				hash_table[s[right_ptr]] = 0
			right_ptr += 1
		return result if result > len(hash_table) else len(hash_table)

if __name__ == "__main__":
	string = 'abcabcbb'
	print(LengthOfLongestSubString.solve(string))
