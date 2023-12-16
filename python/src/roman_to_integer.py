from typing import List


class RomanToInteger:
	@staticmethod
	def solve(s: str) -> int:
		roman_value_map = {
				'I': 1,
				'V': 5,
				'X': 10,
				'L': 50,
				'C': 100,
				'D': 500,
				'M': 1000
		}
		ptr = len(s) -1
		sum = 0
		while ptr >= 0:
			roman_value = roman_value_map[s[ptr]]
			if (ptr + 1) < len(s) and roman_value < roman_value_map[s[ptr + 1]]:
				sum -= roman_value
			else:
				sum += roman_value
			ptr -= 1
		return sum

if __name__ == "__main__":
	print(RomanToInteger.solve2("III"))
	print(RomanToInteger.solve2("XIV"))
