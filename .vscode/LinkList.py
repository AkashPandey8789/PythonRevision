class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.header = None

    def addNode(self, Node):
        if self.header:
            cur = self.header
            while cur.next:
                cur = cur.next
            cur.next = Node
        else:
            self.header = Node

    def linkListTraversal(self):
        if self.header:
            cur = self.header
            while cur:
                print(cur.data)
                cur = cur.next
        else:
            print("No Data")


node = Node(5)
linkList = LinkList()
linkList.addNode(node)

linkList.linkListTraversal()
