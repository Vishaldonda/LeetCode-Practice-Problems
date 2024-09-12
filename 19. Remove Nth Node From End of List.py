class Node:
    def __init__(self,data=0,next=None) -> None:
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
        
    
    def remove_node(self,n):
        
        dummy = Node()
        first = dummy
        second = dummy
        dummy.next = self.head
        
        while (n>=0):        
            first = first.next
            n-=1
                        
        while (first):
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        self.head = dummy.next



l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)

# remove nth node
n = 2
l1.remove_node(n)
l1.print_list()

