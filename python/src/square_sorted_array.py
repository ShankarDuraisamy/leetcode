from typing import List


class SortedNumSquare:
	@staticmethod
	def solve(nums: List[int]) -> List[int]:
		left_ptr = 0
		right_ptr = len(nums) -1
		temp = 0
		result = []
		for i, n in enumerate(nums):
			nums[i] = n * n
		while left_ptr <= right_ptr:
			if nums[left_ptr] > nums[right_ptr]:
				result.append(nums[left_ptr])
				left_ptr += 1
			else:
				result.append(nums[right_ptr])
				right_ptr -= 1

		return result[::-1]

if __name__ == "__main__":
	print(SortedNumSquare.solve([-4,-1,0,3,10]))
