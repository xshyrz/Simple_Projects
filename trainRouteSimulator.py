class StationNode:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
 
class OzTrainRouteSimulator:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def AddStationAtStart(self, name):
        new_node = StationNode(name)
 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            print(f"-> Added Station '{name}' in an empty route.\n")
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head = new_node
            print(f"-> Added Station '{name}' at the start of the route.\n")
        self.size += 1
 
    def AddStationAtEnd(self, name):
        new_node = StationNode(name)
 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            print(f"-> Added Station '{name}' in an empty route.\n")
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
            print(f"-> Added Station '{name}' at the end of the Route.\n")
        self.size += 1
 
    def InsertStationAfter(self, target, name):
        if self.head is None:
            print("Error: Route is empty.\n")
            return
 
        target_route = self.head
        found = False
 
        while True:
            if target_route.data == target:
                found = True
                break
 
            target_route= target_route.next
            if target_route == self.head:
                break
 
        if not found:
            print(f"Error: Target node '{target}' is not found in the list.\n")
 
        if target_route == self.tail:
            self.insert_at_end()
 
        new_node = StationNode(name)
        node_after_target = target_route.next
 
        new_node.next = node_after_target
        new_node.prev = target_route
        node_after_target.prev = new_node
        target_route.next = new_node
 
        self.size += 1
 
        print(f"-> Added '{name}' after '{target_route.data}'.\n")
 
    def DeleteLastStation(self):
        if self.tail is None:
            print("Error: Route is empty.\n")
            return
 
        deleted_data = self.tail.data
 
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print(f" -> Deleted '{deleted_data}' from the route.\n")
        else:
            self.tail = self.tail.prev
            self.head.prev = self.tail
            self.tail.next = self.head
            print(f" -> Deleted '{deleted_data}' from the list.\n")
        self.size -= 1
 
    def TraverseForward(self):
        if self.head is None:
            print("Error: Route is empty.\n")
            return
 
        current = self.head
        output = []
        start_node = self.head
 
        while current:
            output.append(str(current.data))
            current = current.next
            if current == start_node:
                break
        print("Clockwise Route:\n", output)
 
    def TraverseBackward(self):
        if self.tail is None:
            print("Error: Route is empty.\n")
            return
 
        current = self.tail
        output = []
        start_node = self.tail
 
        while current:
            output.append(str(current.data))
            current = current.prev
            if current == start_node:
                break
 
        print("Counter-Clockwise Route:\n", output)
 
    def FindStation(self, target):
        if self.head is None:
            print("Error: Route is empty.\n")
            return
 
        current = self.head
        found = False
 
        while True:
            if current.data == target:
                found = True
                break
 
            current = current.next
            if current == self.head:
                break
 
        if found:
            print(f"-> Searched for '{target}': FOUND.\n")
        else:
            print(f"-> Searched for '{target}': NOT FOUND.\n")
 
    def ShowCurrentRouteStatus(self):
        if self.head is None:
            print("Error: Route is empty.\n")
            return
 
        print("Current Route Status:")
        print(f" - First Station: {self.head.data}")
        print(f" - Last Station: {self.tail.data}")
        print("Route is circular and stable")