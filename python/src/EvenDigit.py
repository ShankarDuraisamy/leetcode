from typing import List


class EvenDigit:
	@staticmethod
	def solve(nums: List[int]) -> int:
		result = 0
		count = 0
		for i, n in enumerate(nums):
			while n > 0:
				count += 1
				n = int(n/10)
			result += 1 if count %2 == 0 else 0
			count = 0
		return result


if __name__ == "__main__":
	print(EvenDigit.solve([437,315,322,431,686,264,442]))
