from typing import List


class MaxConsecutiveOnes:
	@staticmethod
	def solve(nums: List[int]) -> int:
		right_ptr = 0
		result = 0
		count = 0
		while right_ptr < len(nums):
			if nums[right_ptr] == 1:
				while right_ptr < len(nums) and nums[right_ptr] == 1:
					count += 1
					right_ptr += 1
				result = result if result > count else count
				count = 0
			right_ptr += 1
		return result

	@staticmethod
	def solve2(nums: List[int]) -> int:
		right_ptr = 0
		result = 0
		count = 0
		while right_ptr < len(nums):
			if nums[right_ptr] == 1:
				count += 1
			else:
				count = 0
			result = result if result > count else count
			right_ptr += 1
		return result







if __name__ == "__main__":
	print(MaxConsecutiveOnes.solve([1,1,0,1,1,1]))
