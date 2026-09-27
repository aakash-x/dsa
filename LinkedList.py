# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
            
    def __init__(self, nums:list[int]=[]):
        self.head = Node(None, None)
        for item in nums:
            self.add(item)
    
    def add(self, val):
        curr = self.head
        while curr.next != None:
            curr = curr.next;
        curr.next = Node(val, None)

    def traverse(self):
        curr = self.head.next;
        if not curr:
            print("No items in the LinkedList")
            return
        print("Item of linked list")
        while (curr != None):
            print(curr.val, end = ", ")
            curr = curr.next
        print()
            
    def remove(self, val):
        prev = self.head
        curr = self.head.next
        if not curr:
            print("No items in linkedlist")
            return
        
        while(curr and curr.val != val):
            prev = curr
            curr = curr.next
        
        if(curr == None):
            print(f"Item is not found {val}")
            return None
            
        prev.next = curr.next
            

if __name__ == '__main__':
    ll = LinkedList([4,5,6])
    ll.traverse()
    ll.add(1)
    ll.add(5)
    ll.add(7)
    ll.add(1)
    ll.traverse()
    ll.remove(1)
    ll.remove(5)
    ll.remove(4)
    ll.traverse()
    ll.remove(7)
    ll.traverse()
    ll.remove(8)