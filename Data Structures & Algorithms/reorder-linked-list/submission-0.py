# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
       
        slow = head
        fast = head.next
        
        fast = head.next 
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        pt2 = slow.next
        slow.next = None
        prev = None 
        nxt = None 
        while pt2:
            nxt = pt2.next 
            pt2.next = prev
            prev = pt2
            pt2 = nxt 
        first = head 
        second = prev 
        while second:
            temp1 = first.next 
            temp2 = second.next 
            first.next = second
            second.next = temp1 
            first = temp1
            second = temp2
            


        

        