class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkList:
    def __init__(self):
        self.header = None

    def addNode(self, Node):
        if self.header:
            cur = self.header
            while cur.next:
                cur = cur.next
            cur.next = Node
            Node.prev = cur
        else:
            self.header = Node

    def traverseList(self):
        if self.header:
            cur = self.header
            while cur:
                print(cur.data)
                cur = cur.next
        else:
            print("No Data!!")

    def deleteNode(self, Node):
        if self.header:
            print("Node", Node.data)
            print("Head", self.header.data)
            print("Type ", type(self.header.data))
            print(type(Node.data))
            if int(self.header.data) == int(Node.data):
                print("HERE!!")
                cur = self.header.next
                cur.prev = None
                self.header = cur


dlist = DoubleLinkList()
for i in range(5):
    n = input("Enter element:")
    dlist.addNode(Node(n))


dlist.traverseList()
dlist.deleteNode(Node(5))
