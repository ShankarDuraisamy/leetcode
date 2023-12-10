from typing import List


class MedianSortedArray:
	@staticmethod
	def solve1(nums1: List[int], nums2: List[int]) -> float:
		first_ptr = 0
		second_ptr = 0
		result_ptr = 0
		result = []
		itr_ctl = len(nums1) + len(nums2)
		itr_ctl = int(itr_ctl/2) if int(itr_ctl%2) == 0 else int(itr_ctl/2) + 1
		while result_ptr <= itr_ctl and (first_ptr < len(nums1) or second_ptr < len(nums2)):
			if first_ptr < len(nums1) and second_ptr < len(nums2):
				if nums1[first_ptr] < nums2[second_ptr]:
					result.append(nums1[first_ptr])
					first_ptr += 1
				else:
					result.append(nums2[second_ptr])
					second_ptr += 1
			elif first_ptr < len(nums1):
				result.append(nums1[first_ptr])
				first_ptr += 1
			elif second_ptr < len(nums2):
				result.append(nums2[second_ptr])
				second_ptr += 1
			result_ptr += 1
		return (result[result_ptr-2] + result[result_ptr-1])/2 if (len(nums1) + len(nums2)) % 2 == 0 else result[result_ptr-2]

	def solve2(nums1: List[int], nums2: List[int]) -> float:
		first_ptr = 0
		second_ptr = 0
		result = []
		itr_ctl = len(nums1) + len(nums2)
		itr_ctl = int(itr_ctl / 2) if int(itr_ctl % 2) == 0 else int(itr_ctl / 2) + 1
		count = 0
		while first_ptr < len(nums1) and second_ptr < len(nums2) and count<=itr_ctl:
			if nums1[first_ptr] < nums2[second_ptr]:
				result.append(nums1[first_ptr])
				first_ptr += 1
			else:
				result.append(nums2[second_ptr])
				second_ptr += 1
			count += 1

		while first_ptr < len(nums1) and count <= itr_ctl:
			result.append(nums1[first_ptr])
			first_ptr += 1
			count += 1

		while second_ptr < len(nums2) and count <= itr_ctl:
			result.append(nums2[second_ptr])
			second_ptr += 1
			count += 1
		return (result[count - 2] + result[count - 1]) / 2 if (len(nums1) + len(nums2)) % 2 == 0 else result[count - 2]



if __name__ == "__main__":
	print(MedianSortedArray.solve2([1,2], [3]))
