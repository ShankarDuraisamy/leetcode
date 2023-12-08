from typing import List


class PalindromeNumber:
	@staticmethod
	def solve(x: int) -> bool:
		str_num = str(x)
		left_ptr = 0
		right_ptr = len(str_num) - 1
		while left_ptr < len(str_num)/2:
			if str_num[left_ptr] != str_num[right_ptr]:
				return False
			left_ptr += 1
			right_ptr -= 1
		return True

	@staticmethod
	def solve2(x: int) -> bool:
		if x == 0 | x % 10 == 0:
			return False
		x1 = x
		result = 0
		while x1 > 0:
			result = (result * 10) + (x1 % 10)
			x1 = int(x1/10)
		if result == x:
			return True
		return False



if __name__ == "__main__":
	print(PalindromeNumber.solve2(121))
