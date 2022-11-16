#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example 1:
#Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
 #Explanation: 342 + 465 = 807.



class solution:
    def addTwoNumbers(self, l1:optional[ListNode], l2: optional[ListNode] -> optional[ListNode]):
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 or l2:
            val1 = l1.va if l1 else 0
            val2 = l2.va if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(out)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if(carry > 0):
            curr.next = ListNode(carry)
        return dummyHead.next
