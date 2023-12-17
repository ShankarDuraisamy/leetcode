from typing import List
from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class ListMerge:
	@staticmethod
	def solve(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		result = ListNode()
		ptr = result
		while list1 or list2:
			if list1 is None:
				ptr.next = list2
				return result.next
			elif list2 is None:
				ptr.next = list1
				return result.next
			elif list1.val <= list2.val:
				ptr.next = list1
				list1 = list1.next
			else:
				ptr.next = list2
				list2 = list2.next
			ptr.next.next = None
			ptr = ptr.next
		return result.next

def test_data(inp: List[int]):
	ll = None
	temp_node = None
	for i, n in enumerate(inp):
		if ll is None:
			temp_node = ListNode(n, None)
			ll = temp_node
			continue
		temp_node.next = ListNode(n, None)
		temp_node = temp_node.next
	return ll


def print_node(num: ListNode):
	while num is not None:
		print(num.val)
		num = num.next

if __name__ == "__main__":
	#print_node(test_data([1, 2, 4]))
	#print_node(test_data([1, 3, 4]))
	print_node(ListMerge.solve(test_data([1, 2, 4]), test_data([1, 3, 4])))
