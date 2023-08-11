# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#
# # Example usage
# llist = LinkedList()
# llist.append(10)
# llist.append(20)
# llist.append(30)
# llist.display()

class Node:
    '''class Node: Defines a class named Node that represents the basic building block of a linked list.
    Each node has two attributes:
    1.data, which holds the value of the node,
    2. next, which is a reference to the next node in the list.'''
    def __init__(self,data):

        self.data= data  #VALUE
        self.next = None  #REFERENCE

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode= data
        if self.head is None:
            self.head= newNode
        else:
            lastnode= self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode= lastnode.next
            lastnode.next = newNode

    def printList(self):

        currentnode = self.head
        print(currentnode.data)
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode= currentnode.next

Node1 = Node("Abdul")
LinkedList= LinkedList()
LinkedList.insert(Node1)
Node2 = Node("Mohiz")

LinkedList.insert(Node2)
Node3 = Node("Saeed")

LinkedList.insert(Node3)
LinkedList.printList()

