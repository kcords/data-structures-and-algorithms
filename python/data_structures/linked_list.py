class Node:
    def __init__(self, value, next=None):
        """Initializes the creation of a new Node

        Args:
            value (any): Value of the node (typically an int).
            next (Node, optional): Pointer to the next node. Defaults to None.
        """
        self.value = value
        self.next = next


class LinkedList:
    """Creates a new LinkedList"""

    def __init__(self):
        self.head = None

    def __str__(self):
        value_strings = []
        current = self.head
        while current is not None:
            value_strings.append(f"{{ {current.value} }}")
            current = current.next
        value_strings.append("NULL")
        return ' -> '.join(value_strings)

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, val):
        if self.head == None:
            self.head = Node(val)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(val)

    def insert_before(self, val, new_val):
        new_node = Node(new_val)
        current = self.head
        if self.head.value == val:
            new_node.next = self.head
            self.head = new_node
            return
        while current.next is not None:
            if current.next.value == val:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise TargetError(f"{val} not found in linked list")

    def insert_after(self, val, new_val):
        current = self.head
        while current is not None:
            if current.value == val:
                new_node = Node(new_val)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise TargetError(f"{val} not found in linked list")

    def kth_from_end(self, k):
        nodes = []
        current = self.head
        while k >= 0 and current is not None:
            nodes.append(current)
            current = current.next
        if k < 0 or k >= len(nodes):
            raise TargetError(f"{k} is not a valid node")
        kth_node = nodes[-k - 1]
        return kth_node.value

class TargetError(Exception):
    pass

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.kth_from_end(2))
    print(ll.kth_from_end(1))
    print(ll.kth_from_end(0))
