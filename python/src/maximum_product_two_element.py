from typing import List


class MaximumProduct:
	@staticmethod
	def solve(nums: List[int]) -> int:
		first_max = 0
		second_max = 0
		for i, n, in enumerate(nums):
			if n > first_max:
				second_max = first_max
				first_max = n
			if n > second_max:
				second_max = n
		return (first_max -1) * (
				second_max -1)

if __name__ == "__main__":
	print(MaximumProduct.solve([1,5,4,5]))
