from typing import List


class RemoveDuplicate:
	@staticmethod
	def solve(nums: List[int]) -> int:
		count = len(nums)
		left_ptr = 1
		right_ptr = 1
		while right_ptr < len(nums):
			if nums[right_ptr - 1] != nums[right_ptr]:
				nums[left_ptr] = nums[right_ptr]
				left_ptr += 1
			right_ptr += 1
		return left_ptr

if __name__ == "__main__":
	inp = [1, 1, 2]
	print(RemoveDuplicate.solve(inp))
	print(inp)

