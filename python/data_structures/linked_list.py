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

    def some_method(self):
        # method body here
        pass


class TargetError:
    pass
