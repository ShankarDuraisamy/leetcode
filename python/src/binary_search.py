from typing import List


class BinarySearch:
	@staticmethod
	def solve(nums: List[int], target: int) -> int:
		return BinarySearch.recursion(nums, target, 0, len(nums)-1)

	@staticmethod
	def recursion(nums: List[int], target: int, start_location, end_location):
		median = int(end_location -start_location / 2)
		if start_location > end_location:
			return -1
		if nums[median] == target:
			return median
		elif target > nums[median]:
			return BinarySearch.recursion(nums, target, median+1, len(nums)-1)
		else:
			return BinarySearch.recursion(nums, target, 0, median - 1)

	@staticmethod
	def non_recursion(nums: List[int], target: int):
		end_location = len(nums) - 1
		start_location = 0
		while start_location <= end_location:
			median = start_location + int((end_location - start_location) / 2)
			if nums[median] == target:
				return median
			if target > nums[median]:
				start_location = median + 1
			if target < nums[median]:
				end_location = median - 1
		return -1


if __name__ == "__main__":
	print(BinarySearch.solve([1, 2, 3, 4, 5, 9], 9))
