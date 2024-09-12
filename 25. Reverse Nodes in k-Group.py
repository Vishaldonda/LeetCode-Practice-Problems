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

    def reverseInKGroups(self,head,k):
        curr = head
        for _ in range(k):
            if not curr: 
                return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.reverseInKGroups(curr, k)
        
        return prev
        

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

l1.print_list()
k = 2
l1.head = l1.reverseInKGroups(l1.head,k)
l1.print_list()
