
# Define Linked List Node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Convert Python list into Linked List
def createLinkedList(arr):
    dummy = ListNode(0)
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


# Convert Linked List into Python list for printing
def printLinkedList(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = x + y + carry

            digit = s % 10
            carry = s // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


# Input
l1 = [2, 4, 3]
l2 = [5, 6, 4]

# Convert inputs into Linked Lists
linked_l1 = createLinkedList(l1)
linked_l2 = createLinkedList(l2)

# Call function
obj = Solution()
answer = obj.addTwoNumbers(linked_l1, linked_l2)

# Print result
print(printLinkedList(answer))
