# 1st create a Node 
# 2nd Create a LinkedList class for handle the node
# 3nd Write a methods to handle the element like insert, delete,print, Count no of element etc..

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head  # [34 ---> 45---> 56 ] 

    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty!")

        itr = self.head
        llstr = ''  
        while itr:
            llstr += str(itr.data) + "---->"
            itr = itr.next #[ 23, 45 , 87 , 56]

        print(llstr)

    def insert_at_end(self,data): # [23, 45, 67, 87]
        if self.head is None:
            self.head = Node(data,None)

        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining("lithi")
    ll.insert_at_begining("Lokesh")
    ll.print()
        




