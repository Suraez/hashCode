# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        while l1:
            s1 += l1.val
            l1 = l1.next
        s2 = ""
        while l2:
            s2 += l2.val
            l2 = l2.next
        rSum = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        return createLinkedList(rSum)


# n1 = ListNode('3')
# n2 = ListNode('4', n1)
# n3 = ListNode('2', n2)

# n4 = ListNode('4')
# n5 = ListNode('6', n4)
# n6 = ListNode('5', n5)

def createLinkedList (str):
    if len(str) == 1:
        return ListNode(str)
    else:
        return ListNode(str[0], createLinkedList(str[1:]))


l1 = createLinkedList('243')
l2 = createLinkedList('564')
s1 = Solution()
ans = s1.addTwoNumbers(l1, l2)

while ans:
    print(ans.val)
    ans = ans.next

# def solution(l1: ListNode):
#     head = l1
#     while head != None:
#         print(head.val)
#         head = head.next

# solution(n3)




