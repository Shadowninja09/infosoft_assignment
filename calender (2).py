class Node:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        # if the starting time of the new event is greater than equals to the ending time of the previous event
        if node.start >= self.end:
            # if there is no new event just after the previous event then we book the new event after the
            # previous event
            if not self.right_child:
                self.right_child = node
                return True
            # if there is an adjacent booking then we look whether the booking can done before or after the adjacent
            # booking
            return self.left_child.insert(node)
        # if the starting time of the previously booked event is greater than equals to the ending time of the new event
        elif self.start >= node.end:
            # if there is no new event just before the previously booked event then we book the event putting it
            # before the previous event
            if not self.left_child:
                self.left_child = node
                return True
            # if there is an adjacent booking then we look whether the booking can done before or after the adjacent
            # booking
            return self.left_child.insert(node)
        else:
            # if the condition fails that means there is overlapping of events which means we cannot book the new event
            return False


class Calendar:
    def __init__(self):
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        # if there is no booking then we book the event
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        # if there is a previous booking then we use the insert method to check whether the new event timings overlap
        # with the previous booking
        return self.root.insert(node=Node(start, end))


calendar = Calendar()

print(calendar.book(5, 10))
print(calendar.book(8, 13))
print(calendar.book(10, 15))