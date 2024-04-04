class ListLinked:
    class Node:
        def __init__(self, val):
            self.value = val
            self.next = None
            
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
            return
        iter = self.head
        while iter.next:
            iter = iter.next
        iter.next = self.Node(data)

    def show(self):
        iter = self.head
        print('Starting==')
        while iter:
            print(f'item:{iter.value}')
            iter = iter.next
        print('Ending==')

    def reserve(self):
        # None-head(1)-(Fred)-(8)-(Fei)-None
        if not self.head or not self.head.next:
            return
        pre = None
        curr = self.head
        #save_next = self.head.next
        while curr:
            save_next = curr.next
            curr.next = pre
            pre = curr
            curr = save_next
        self.head = pre

    def reserve_by_stack(self):
        stack = []
        cur = self.head
        while cur:
            stack.append(cur)
            cur = cur.next
        new_head = stack.pop()
        new_cur = new_head
        while stack:
            new_cur.next = stack.pop()
            new_cur = new_cur.next
        #Notice last node's next shall be set None explictly, or it may end loop !!!
        new_cur.next = None
        self.head = new_head

ll = ListLinked()
ll.append(1)
ll.append('Fred')
ll.append(8)
ll.append('Fei')
ll.show()
print('=============after reserve')
ll.reserve()
ll.show()
print('=============after reserve + reserve')
ll.reserve_by_stack()
ll.show()