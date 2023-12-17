from typing import List


class ValidParentheses:
	@staticmethod
	def solve(s: str) -> bool:
		bras_map = {
					']' : '[',
					'}' : '{',
					')' : '('
					}
		stack = []
		for ch in s:
			if ch in bras_map:
				if stack and stack[-1] == bras_map[ch]:
					stack.pop()
				else:
					return False
			else:
				stack.append(ch)
		return True if len(stack) == 0 else False

	def solve1(s: str) -> bool:
		stack = []
		for ch in s:
			if ch in {'(', '{', '['}:
				stack.append(ch)
			elif len(stack) == 0:
				return False
			else:
				char = stack.pop()
				if (ch == ')' and char == '(') or (ch == '}' and char == '{') or (ch == ']' and char == '['):
					continue
				return False
		return True




if __name__ == "__main__":
	print(ValidParentheses.solve("()[]{}"))
