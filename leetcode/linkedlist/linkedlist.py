# Definition of a singly linked list 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
# Reversing a linkedlist
class Solution:

    """
    Reverse linked list
    Intuition : Store next pointer in tmp variable before the link is broken to continue traversing the array
    """
    def reverseList(self, head: ListNode) -> ListNode: 
        prev, cur = None, head 

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur 
            cur = tmp 
        
        return prev 

    def recursiveReverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None 
        
        newHead = head 
        if head.next:
            # reverse the linked list next to the head
            # the self is needed here
            newHead = self.recursiveReverseList(head.next)
            # after reversing, head.next is now pointing to the tail
            # we append head to the tail
            head.next.next = head 
            # ensure that we dont have a cyclical list
            head.next = None

        
        return newHead        
    
    """
    Merge Two Sorted Lists
    Intuition : Have a dummy node, then just iterate through both linked lists and append the smaller node to the dummy node. 
                Benefits of using a dummy node is so that in the end we can just return dummy.next and simplifies the logic of merging 2 linked lists.
    """
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # cur pointer allows us to traverse our result linkedlist to continue adding nodes to it
        dummy = cur = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1 
                list1 = list1.next 
            else:
                dummy.next = list2
                list2 = list2.next

        if list1:
            cur.next = list1 
        elif list2:
            cur.next = list2 
        
        return dummy.next 
    
    def recursiveMergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2 
        if not list2:
            return list1 

        if list1.val <= list2.val:
            list1.next = self.recursiveMergeTwoLists(list1.next, list2)
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


    """
    Linked List Cycle detection
    Intuition : Have a fast and slow pointer, if at any point they point to the same node, this means that there is a cycle
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True 
        
        return False

    """
    Remove Node From End of Linked List
    Intuition : It is obvious to do it in 2 passes but not an easy to do in 1 pass.
                To do in 1 pass, have a fast pointer and a slow pointer. 
                Give the fast pointer a headstart of n.
                Move both the slow and fast pointer until the fast pointer reaches end of array.
                The slow pointer will then point to the node to be removed.
                Use a dummy node for easier handle edge case of allowing the slow pointer to start 1 position behind so that it is properly aligned.
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        slow = dummy 
        fast = head 
        
        # giving the fast pointer the headstart
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next 
        
        slow.next = slow.next.next 

        return dummy.next