class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            print(f" -> Added '{data}' in an empty list.")
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.head = new_node
            print(f" -> Added '{data}' at the start of the circular list.")

        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            print(f" -> Added '{data}' in an empty list.")
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
            print(f" -> Added '{data}' at the end of the circular list.")

        self.size += 1

    def inserting_after_node(self, target_data, data):
        if self.head is None:
            print("Error: List is empty.")
            return
        
        target_node = self.head
        found = False
        
        while True:
            if target_node.data == target_data:
                found = True
                break
            target_node = target_node.next
            
            if target_node == self.head:
                break
        
        if not found:
            print("Error: Not found!")
            return
        
        if target_node == self.tail:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        node_after_target = target_node.next                       
        new_node.next = node_after_target
        new_node.prev = target_node                    
        node_after_target.prev = new_node
        target_node.next = new_node

        self.size += 1 
        print(f" -> Added '{data}' after '{target_data}' node.")
        
    def inserting_before_node(self, target_data, data):
        if self.head is None:
            print("Error: List is empty.")
            return
        
        target_node = self.head
        found = False
        
        while True:
            if target_node.data == target_data:
                found = True
                break
            target_node = target_node.next
            
            if target_node == self.head:
                break
        
        if not found:
            print("Error: Not found!")
            return
        
        if target_node == self.tail:
            self.insert_at_start(data)
            return
        
        new_node = Node(data)
        node_before_target = target_node.prev                     
        new_node.prev = node_before_target
        new_node.next = target_node                    
        node_before_target.next = new_node
        target_node.prev = new_node

        self.size += 1 
        print(f" -> Added '{data}' before '{target_data}' node.")
        
    def traversing_forward(self):
        if self.head is None:
            print("Error: List is empty.")
            return

        temp = self.head
        output = []
        start_node = self.head

        while True:
            output.append(str(temp.data))
            temp = temp.next
            if temp == start_node:
                break
        print(f"Forward Traversal: {output} <-> HEAD")

    def traversing_backward(self):
        if self.head is None:
            print("Error: List is empty.")
            return

        temp = self.tail
        output = []
        start_node = self.tail

        while True:
            output.append(str(temp.data))
            temp = temp.prev
            if temp == start_node:
                break
        print(f"Backward Traversal: -> {output} <-> TAIL")


if __name__ == "__main__":
    cll = CircularLinkedList()

    print("\n--- Insert at end ---")
    cll.insert_at_end("egg")
    cll.insert_at_end("ham")
    cll.insert_at_end("spam")
    
    print("\n--- Insert at start ---")
    cll.insert_at_start("first")

    print("\n--- Insert after a Node ---")
    cll.inserting_after_node("egg", "hotdog")

    print("\n--- Insert before a Node ---")
    cll.inserting_before_node("ham", "rice")
    
    print("\n--- Traverse Forward ---")
    cll.traversing_forward()

    print("\n--- Traverse Backward ---")
    cll.traversing_backward()