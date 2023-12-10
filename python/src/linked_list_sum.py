from typing import List, Optional

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        
'''


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class LinkedListSum:

	@staticmethod
	def solve(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		head_node = None
		last_node = None
		reminder = 0
		first_num = 0
		second_num = 0
		while l1 is not None or l2 is not None or reminder > 0:
			first_num = l1.val if l1 else 0
			l1 = l1 if l1 is None else l1.next
			second_num = l2.val if l2 else 0
			l2 = l2 if l2 is None else l2.next
			if head_node is None:
				head_node = ListNode()
				last_node = head_node
			else:
				last_node.next = ListNode()
				last_node = last_node.next
			total = first_num + second_num + reminder
			reminder = int(total/ 10) if total > 9 else 0
			total = total - 10 if total > 9 else total
			last_node.val = total
		return head_node


def test_data_generation(num):
	head_node = None
	last_node = None
	while num > 0:
		val = num % 10
		num = int(num / 10)
		if head_node is None:
			head_node = ListNode(val)
			last_node = head_node
		else:
			last_node.next = ListNode(val)
			last_node = last_node.next
	return head_node


def print_node(num: ListNode):
	while num is not None:
		print(num.val)
		num = num.next


if __name__ == "__main__":
	print_node(LinkedListSum.solve(test_data_generation(251), test_data_generation(251)))
