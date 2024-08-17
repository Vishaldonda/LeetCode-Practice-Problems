class Node:
    def __init__(self,data) -> None:
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
    
    def reverse(self):
        if not self.head:
            return 
        
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.head = prev
            

def add_numbers(l1,l2):
        dummy = Node(-1)
        head = dummy
        carry = 0 
        # print(l1.data,l2.data)

        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum+=l1.data
                # print(l1.data)
                l1=l1.next 
            if l2:
                sum+=l2.data
                l2=l2.next 
            
            head.next = Node(sum%10)
            carry = sum//10
            head = head.next
            
        return dummy.next
            

def add_right_order(l1,l2):
    l1.reverse()
    l2.reverse()

    l1.print_list()
    l2.print_list()

    # print(l1.head.data,l2.head.data)
    l3 = LinkedList()
    res_node  = add_numbers(l1.head,l2.head)
    l3.print_node(res_node)

    l3.head = res_node
    l3.reverse()
    l3.print_list()
  


l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(4)

l2 = LinkedList()
l2.append(4)
l2.append(5)
l2.append(6)


add_right_order(l1,l2)


# Case1: digits are stored in reverse order
# l1: 1->2->4
# l2: 4->5->6
#     5->7->0->1


# Case2: digits are stored in right order
#   1->2->4
#   4->5->6
#   5->8->0

