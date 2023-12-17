from typing import List


class RemoveElements:
	@staticmethod
	def solve(nums: List[int], val: int) -> int:
		left_ptr = 0
		right_ptr = 0
		while right_ptr < len(nums):
			if nums[right_ptr] != val:
				nums[left_ptr] = nums[right_ptr]
				left_ptr += 1
			right_ptr += 1
		return left_ptr

if __name__ == "__main__":
	inp = [3,2,2,3]
	print(inp)
	print(RemoveElements.solve(inp, 3))
	print(inp)

