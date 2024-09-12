# Input:  1->2->3->4
# Output: 2->1->4->3

class Node:
    def __init__(self,data=0) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next 
            temp.next = Node(data)
            
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data,end=' -> ')
            curr = curr.next
        print("None")
    
    def print_node(self,curr):
        while curr:
            print(curr.data,end=' -> ')
            curr = curr.next
        print("None")


    def reverseInPairs(self):
        
        if not self.head or not self.head.next: 
            return self.head
        
        dummy = Node()
        dummy.next = self.head
        prev = dummy
        curr = self.head
        
        while curr and curr.next:
            first = curr
            second = curr.next
            
            prev.next = first.next
            first.next = second.next 
            second.next = first
            
            prev = first
            curr = first.next
        
        
        self.head = dummy.next
        return self.head   
    

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

l1.print_list()
node  = l1.reverseInPairs()
# l1.print_node(node)
l1.print_list()
