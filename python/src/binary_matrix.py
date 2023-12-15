from typing import List

# Not Working Please check


class BinaryMatrix:
	@staticmethod
	def solve(nums: List[List[int]]) -> int:
		count = 0
		for i in range(0, len(nums)):
			row_sum = 0
			colum_sum = 0
			row_itr = 0
			colum_itr = 0
			while row_itr < len(nums[i]):
				if i == row_itr:
					row_itr += 1
					continue
				row_sum += nums[i][row_itr]
				row_itr += 1
			while colum_itr < len(nums):
				colum_sum += nums[colum_itr][i]
				colum_itr += 1
			count += 1 if row_sum + colum_sum == 1 else 0
		return count


if __name__ == "__main__":
	print(BinaryMatrix.solve([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))

