class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        """Print the entire linked list."""
        if not self.head:
            print("The list is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node from the list (1-based index)."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be 1 or greater.")

        # Deleting the head node
        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        temp = self.head
        for i in range(n - 2):
            if temp.next is None:
                raise IndexError("Index out of range.")
            temp = temp.next

        if temp.next is None:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n} with value {temp.next.data}")
        temp.next = temp.next.next


# Test the LinkedList 

# Create list and add nodes
ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.add_node(val)

print("Original List:")
ll.print_list()

# Delete 3rd node
try:
    ll.delete_nth_node(3)
    print("List after deleting 3rd node:")
    ll.print_list()
except Exception as e:
    print("Error:", e)

# Delete an invalid node 
try:
    ll.delete_nth_node(10)  #10th node
except Exception as e:
    print("Error:", e)

# Delete from empty list
try:
    empty_list = LinkedList()
    empty_list.delete_nth_node(1)
except Exception as e:
    print("Error:", e)
