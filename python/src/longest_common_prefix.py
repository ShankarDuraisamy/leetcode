from typing import List


class LongestCommonPrefix:

	@staticmethod
	def solve(strs: List[str]) -> str:
		res = ""
		for i in range(0, len(strs[0])):
			for s in strs:
				if len(s) == i or s[i] != strs[0][i]:
					return res
			res += strs[0][i]
		return res

if __name__ == "__main__":
	print(LongestCommonPrefix.solve(["flower", "flow", "flight"]))
