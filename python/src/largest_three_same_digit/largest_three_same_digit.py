
class LargestThreeSameDigit:

	@staticmethod
	def solve(self, num: str) -> str:
		left_ptr = 0
		right_ptr = 0
		result = -1
		while right_ptr < len(num):
			while right_ptr < len(num) and num[left_ptr] == num[right_ptr]:
				right_ptr += 1
			if (right_ptr - 1) - left_ptr >= 2:
				result = int(num[left_ptr]) if int(num[left_ptr]) > result else result
			left_ptr = right_ptr
			right_ptr += 1
		return f"{result}{result}{result}" if result > -1 else ""

if __name__ == "__main__":
	LargestThreeSameDigit.solve("33332222")





