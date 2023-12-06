from typing import List


class MissingNumber:
	@staticmethod
	def solve(nums: List[int]) -> int:
		target_sum = len(nums) *(len(nums) + 1)/2
		actual_sum = 0
		for i, n in enumerate(nums):
			actual_sum += n
		return int(target_sum - actual_sum)

	@staticmethod
	def solve2(nums: List[int]) -> int:
		result = len(nums)
		for i in range(len(nums)):
			result += (i - nums[i])
		return int(result)

	@staticmethod
	def solve3(nums: List[int]) -> int:
		result = 0
		for i in range(0, len(nums)):
			result = result ^ nums[i]
		print(result)
		for i in range(0, len(nums) + 1):
			result = result ^ i
		print(result)

		return result

if __name__ == "__main__":
	print(MissingNumber.solve3([0,1,3]))
