class Solution:
    def insertionSortList(self, head):
        if not head:
            return None

        dummy = ListNode(0)   # helps in insertion
        curr = head

        while curr:
            nxt = curr.next   # store next node
            prev = dummy

            # find position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # insert node
            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return dummy.next

arr = [4,2,1,3]   # Input
print("Input:", arr)

head = list_to_linkedlist(arr)               # list → linked list
sorted_head = Solution().insertionSortList(head)  # sort
result = linkedlist_to_list(sorted_head)     # linked list → list

print("Output:", result)
