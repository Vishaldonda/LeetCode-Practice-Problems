# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
import heapq

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
              
              
    def mergeKLists(self,list_nodes):
        
        pq= []
        
        for ind,node in enumerate(list_nodes):
            if node:
                heapq.heappush(pq, (node.data,ind,node)) # Push( node val, list index, node itself)
        
        dummy = Node()
        curr = dummy
        while(pq):
            val,ind,node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(pq, (node.next.data,ind,node.next))
            
        print(pq)
            
        return dummy.next
    

l1 = LinkedList()
l1.append(1)
l1.append(4)
l1.append(5)

l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)

l3 = LinkedList()
l3.append(2)
l3.append(6)


l1.print_list()
l2.print_list()
l3.print_list()

ll = LinkedList()

list_nodes = [l1.head,l2.head,l3.head]
merged_head  = ll.mergeKLists(list_nodes)

ll.print_node(merged_head)

