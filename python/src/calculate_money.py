from typing import List


class CalculateMoney:
	@staticmethod
	def solve(n: int) -> int:
		no_of_weeks = int(n / 7)
		last_week_days = n % 7
		saving = 0
		if no_of_weeks > 0:
			start = 21
			for i in range(1, no_of_weeks + 1):
				saving += start + i * 7
		if last_week_days > 0:
			start = no_of_weeks + 1
			for i in range(0, last_week_days):
				saving += start + i
		return saving




if __name__ == "__main__":
	print(CalculateMoney.solve(20))
