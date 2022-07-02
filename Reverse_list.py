class ListNode:
    def __init__(self,val=0,nxt=None) -> None:
        self.val = val
        self.next = nxt

def reorder_students(L:ListNode)->ListNode:
    
    slow, fast = L, L

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 1->2->3->4->5->6->7->8
    head = slow
    prev = None
    while head:
        dummy = head.next
        head.next = prev
        prev = head
        head = dummy
    
    return prev
    
    # 1->2->3->4->5->6->7->8 | prev | head | dummy 
    # 1->2->3->4  5->6->7->8 | None | 5 | None
    # 1->2->3->4  5<-6  7->8 | 5 | 6 | 7
    # 1->2->3->4->5->6->7->8 | prev | head | dummy
    # 1->2->3->4->5->6->7->8 | prev | head | dummy

if __name__ == '__main__':
    
    head = ListNode(1,ListNode(2, ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8,ListNode(9,ListNode(10))))))))))

    root = reorder_students(head)
    result = ""
    while root:
        result += f"({root.val})-"
        root = root.next
    result += "None"
    print(result)
