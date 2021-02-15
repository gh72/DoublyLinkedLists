class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous =  None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):

        actual_node =  self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node  = self.tail

        while actual_node is not None:

            print("%d" % actual_node.data)
            actual_node = actual_node.previous


if __name__ == '__main__':

    list = DoublyLinkedList()
    list.insert_end(1)
    list.insert_end(2)
    list.insert_end(3)

    list.traverse_forward()
    list.traverse_backward()
