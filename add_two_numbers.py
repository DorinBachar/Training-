# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current= head
        carry = 0

        while(l1 != None or l2 != None or carry != 0):
            if l1:
                l1_value = l1.val
            else:
                l1_value = 0
        
            if l2:
                l2_value = l2.val
            else:
                l2_value = 0

            sum = l1_value + l2_value +carry
            current.next = ListNode(sum % 10)
            carry = sum // 10

            if l1:
                l1 = l1.next
            else:
                None

            if l2:
                l2 = l2.next
            else:
                None
            current = current.next

        return head.next

            


        
        
