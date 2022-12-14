# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dh = ListNode()
        dh.next = head
        runner = dh
        out1 = ListNode()
        runner1 = out1

        while runner.next:
            if runner.next.val >= x:
                temp = ListNode(runner.next.val)
                runner1.next = temp
                runner1 = runner1.next
                runner.next = runner.next.next
            else:
                runner = runner.next

        runner.next = out1.next

        return dh.next
