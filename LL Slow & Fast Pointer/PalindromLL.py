'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head

        while fast!=None and fast.next != None:
            slow=slow.next
            fast= fast.next.next

            if slow==fast:
                slow=head
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next
                
        return True