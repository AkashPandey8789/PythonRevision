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
            if self.header.data == Node.data:
                print("HERE!!")
                cur = self.header.next
                cur.prev = None
                self.header = cur
            else:
                cur = self.header
                while cur.data != Node.data:
                    cur = cur.next
                if cur.next == None:
                    curPrev = cur.prev
                    curPrev.next = None
                else:
                    curPrev = cur.prev
                    curNext = cur.Next
                    curPrev.next = curNext
                    curNext.prev = curPrev


dlist = DoubleLinkList()
for i in range(5):
    n = input("Enter element:")
    dlist.addNode(Node(n))


dlist.traverseList()
dlist.deleteNode(Node(5))
