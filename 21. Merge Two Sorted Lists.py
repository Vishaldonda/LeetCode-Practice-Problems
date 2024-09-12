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
              
              
    def mergeTwoLists(self,l1, l2):
        
        dummy = Node()
        temp = dummy
        
        while(l1 and l2):
            # print(l1.data,l2.data)
            if l1.data<l2.data:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        while l1:
            dummy.next = l1
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            dummy.next = l2
            dummy = dummy.next
            l2 = l2.next
        
        self.head = temp.next
            
    

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(4)

l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)

l1.print_list()
l2.print_list()

l3 = LinkedList()
l3.mergeTwoLists(l1.head,l2.head)
l3.print_list()

