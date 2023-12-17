from typing import List


class DestinationCity:
	@staticmethod
	def solve(nums: List[List[str]]) -> str:
		hash_table = {}
		for i, n, in enumerate(nums):
			if nums[i][0] not in hash_table:
				hash_table[nums[i][0]] = nums[i][1]

		for i, n, in enumerate(nums):
			for j, city, in enumerate(n):
				if city not in hash_table:
					return city
		return ""

	@staticmethod
	def solve2(paths: List[List[str]]) -> str:
		memory = set()
		for i, path, in enumerate(paths):
			memory.add(path[0])

		for i, path, in enumerate(paths):
			if path[1] not in memory:
				return path[1]
		return ""

	@staticmethod
	def solve3(paths: List[List[str]]) -> str:
		hash_table = {}
		for i, path, in enumerate(paths):
			hash_table[path[0]] = path[1]
		for j, city, in enumerate(hash_table.values()):
			if city not in hash_table:
				return city


if __name__ == "__main__":
	print(DestinationCity.solve3([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
