from typing import List


class SearchInsertPosition:
	@staticmethod
	def solve(nums: List[int], target: int) -> int:
		start_location = 0
		end_location = len(nums) -1
		while start_location <= end_location:
			median = start_location + int((end_location - start_location) / 2)
			if target == nums[median]:
				return median
			elif target > nums[median]:
				start_location = median + 1
			else:
				end_location = median - 1
			median = int((start_location + end_location)/2)
		return median if target < nums[median] else median + 1


if __name__ == "__main__":
	print(SearchInsertPosition.solve([1,3,4,5,6], 3))


