# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None  # Reference to the previous node
#         self.next = None  # Reference to the next node
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None  # Reference to the first node in the list
#
#     def append(self, data):
#         """Append a new node with the given data to the end of the list."""
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#             new_node.prev = current
#
#     def insert_after(self, prev_node, data):
#         """Insert a new node with the given data after the specified node."""
#         if prev_node is None:
#             return
#         new_node = Node(data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node
#         new_node.prev = prev_node
#         if new_node.next:
#             new_node.next.prev = new_node
#
#     def delete(self, target_data):
#         """Delete the first occurrence of the node with the given data."""
#         current = self.head
#         while current:
#             if current.data == target_data:
#                 if current.prev:
#                     current.prev.next = current.next
#                 else:
#                     self.head = current.next
#                 if current.next:
#                     current.next.prev = current.prev
#                 return
#             current = current.next
#
#     def display(self):
#         """Display the data of all nodes in the list."""
#         current = self.head
#         while current:
#             print(current.data, end=" <-> ")
#             current = current.next
#         print("None")
#
# # Example usage
# dllist = DoublyLinkedList()
# dllist.append(10)
# dllist.append(20)
# dllist.append(30)
# dllist.display()
#
# dllist.insert_after(dllist.head, 15)
#
# dllist.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList():
    def __init__(self):
        self.head=None


    def append(self,data):
        #This condition checks if the head attribute of the linked list object (self.head) is None
        if self.head is None:
            # Inside the if block, a new Node object is created with the provided data. This node will be the first node in the linked list.
            new_node = Node(data)
            '''Since this is the first node, its prev reference is set to None, 
            indicating that there is no previous node before it.'''
            new_node.prev = None
            self.head=new_node

        else:
            new_node=Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev=cur
            new_node.next=None

    def displayList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

dlist=DoublyLinkedList()
dlist.append(20)
dlist.append(30)
dlist.append(40)
dlist.append(50)
dlist.displayList()