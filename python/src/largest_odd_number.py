from typing import List


class LargestOddNumber:
	@staticmethod
	def solve(num: str) -> str:
		right_ptr = len(num) - 1
		while right_ptr != -1:
			if int(num[right_ptr]) % 2 != 0:
				return num[0:right_ptr + 1]
			right_ptr += 1

		return ""


if __name__ == "__main__":
	num = "54"
	print(LargestOddNumber.solve("52"))
