'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.The list should be made by 
splicing together the nodes of the first two lists. Return the head 
of the merged linked list.

EX1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

EX2: 
Input: list1 = [], list2 = []
Output: []

EX#:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

'''


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        if l1.val >= l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
