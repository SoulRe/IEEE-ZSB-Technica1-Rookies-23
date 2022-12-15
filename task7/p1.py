# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""i tried my best to debug this code so i understand what's happening in most of it"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node =newlist =  ListNode()
        print(node)
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                print(node)
                list1 , node = list1.next, list1
                print(node)
            else:
                node.next = list2
                list2, node = list2.next, list2
                print(node)
        
        if list1 or list2:
            node.next = list1 if list1 else list2

        return newlist.next