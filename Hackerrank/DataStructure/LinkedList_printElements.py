
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

def printLinkedList(head):
    singlyLinkedList = SinglyLinkedList()
    singlyLinkedList.head = head
    current_node = singlyLinkedList.head
    while current_node:
        print(current_node.data, end='\n')
        current_node = current_node.next