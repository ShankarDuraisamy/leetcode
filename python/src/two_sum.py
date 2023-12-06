from typing import List


class TwoSum:
	@staticmethod
	def solve(nums: List[int], target: int) -> List[int]:
		hash_table = {}
		for i, n, in enumerate(nums):
			diff = target - n
			if diff in hash_table:
				return [hash_table.get(diff), i]
			else:
				hash_table[n] = i

if __name__ == "__main__":
	print(TwoSum.solve([2,7,11,15], 9))
