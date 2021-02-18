# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        while l1 != None:
            s1 += l1.val
            l1 = l1.next
        s2 = ""
        while l2 != None:
            s2 += l2.val
            l2 = l2.next

        sum = int(s1[::-1]) + int(s2[::-1])
        mSum = str(sum)[::-1]
        print(mSum)
        # for i in range(0,mSum):
        #     if i == len(sum) -1 :
        #         pass
        #     else:
        #         n1 = ListNode(num, )


n1 = ListNode('3')
n2 = ListNode('4', n1)
n3 = ListNode('2', n2)

n4 = ListNode('4')
n5 = ListNode('6', n4)
n6 = ListNode('5', n5)

s1 = Solution()
s1.addTwoNumbers(n3, n6)

# def solution(l1: ListNode):
#     head = l1
#     while head != None:
#         print(head.val)
#         head = head.next

# solution(n3)




