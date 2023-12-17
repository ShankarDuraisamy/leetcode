from typing import List


class Anagram:
	@staticmethod
	def solve(s: str, t: str) -> bool:
		anagram_table = {}
		if len(s) != len(t):
			return False
		for i, n in enumerate(s):
			if n in anagram_table:
				anagram_table[n] = anagram_table[n] + 1
			else:
				anagram_table[n] = 1

		for i, n in enumerate(t):
			if n in anagram_table and anagram_table[n] > 0:
				anagram_table[n] = anagram_table[n] - 1
			else:
				return False
		return True


	'''
		Not working
	'''

	@staticmethod
	def solve1(s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		sum = 0
		for i, n in enumerate(s):
			sum += ord(n)
			sum -= ord(t[i])
		return True if sum == 0 else False


if __name__ == "__main__":
	print(Anagram.solve1("anagram", "nagaram"))
