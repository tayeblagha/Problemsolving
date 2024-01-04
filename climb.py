class Solution:
    def deleteDuplicatesByInsertion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(head.val)
        current_new = dummy
        current = head

        while current.next:
            if current.val != current.next.val:
                current_new.next = ListNode(current.next.val)
                current_new = current_new.next

            current = current.next

        return dummy
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head