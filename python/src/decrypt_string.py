
class DecryptString:
	@staticmethod
	def solve(s: str) -> str:
		hashmap = {
			'1': 'a',
			'2': 'b',
			'3': 'c',
			'4': 'd',
			'5': 'e',
			'6': 'f',
			'7': 'g',
			'8': 'h',
			'9': 'i',
			'10#': 'j',
			'11#': 'k',
			'12#': 'l',
			'13#': 'm',
			'14#': 'n',
			'15#': 'o',
			'16#': 'p',
			'17#': 'q',
			'18#': 'r',
			'19#': 's',
			'20#': 't',
			'21#': 'u',
			'22#': 'v',
			'23#': 'w',
			'24#': 'x',
			'25#': 'y',
			'26#': 'x'
		}
		itr = 0
		result = ""
		print(len(s))
		while itr < len(s):
			if len(s) > (itr + 2):
				result += hashmap[s[itr: itr + 3]] if s[itr: itr + 3].endswith('#') else hashmap[s[itr]]
				itr += 3 if s[itr: itr + 3].endswith('#') else 1
			else:
				result += hashmap[s[itr]]
				itr += 1
		return result




if __name__ == "__main__":
	print(DecryptString.solve("10#11#12"))
