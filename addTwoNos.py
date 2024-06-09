# Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   # Input: Two singly-linked lists.
   # Output: A linked list containing sum from the numbers of the Linked list.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode(0)
        tail = tempHead
        carry = 0

        while(l1 != None or l2 != None or carry != 0):
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            sum = num1 + num2 + carry
            digit = sum % 10
            carry = sum // 10

            print(sum," ",digit," ",carry)

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = tempHead.next
        tempHead.next = None
            
        return result
