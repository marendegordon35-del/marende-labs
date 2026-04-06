# Linked list implementation in Python
# data = 20, 40, 60, 80

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create linked list
head = None
# Insert data into linked list
 # time complexity O(n)
 # reason: we have to traverse the linked list to find the last node, which takes O
data_list = [20, 40, 60, 80]
for data in data_list:
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
# Append 100 to the end of the linked list
 # time complexity O(n)
 # reason: we have to traverse the linked list to find the last node, which takes O
new_node = Node(100)
current = head
while current.next:
    current = current.next
current.next = new_node
# Print linked list
current = head
while current:
    print(current.data)
    current = current.next
# prepend 10 to the beginning of the linked list
 # time complexity O(1)
 # reason: we are just creating a new node and updating the head pointer, which takes constant time
new_node = Node(10)
new_node.next = head
head = new_node
# insert 50 after 40
 # time complexity O(n)
 # reason: in the worst case, we may have to traverse the linked list to find the
new_node = Node(50)
current = head
while current.data != 40:
    current = current.next
new_node.next = current.next
current.next = new_node
# print linked list
current = head
while current:
    print(current.data)
    current = current.next
# delete 80 from the linked list
 # time complexity O(n)
 # reason: in the worst case, we may have to traverse the linked list to find the
current = head
while current.next.data != 80:
    current = current.next
current.next = current.next.next
# search for 30 in the linked list
 # time complexity O(n)
 # reason: in the worst case, we may have to visit each node in the linked list
current = head
while current:
    if current.data == 30:
        print("Found 30 in the linked list")
        break
    current = current.next
else:
    print("30 not found in the linked list")
# print linked list
current = head
while current:
    print(current.data)
    current = current.next
# display_print all the elements in the linked list
 # time complexity O(n)
 # reason: visiting each node in the linked list once to print its data, where n is the number of nodes in the linked list
current = head
while current:
    print(current.data)
    current = current.next
# is empty
 # time complexity O(1)
 # reason: we are just checking if the head is None or not, which takes constant time
if head is None:
    print("Linked list is empty")
else:  
    print("Linked list has elements")
# size of linked list
 # time complexity O(n)
 # reason: we have to traverse the linked list to count the number of nodes, which takes
size = 0
current = head
while current:
    size += 1
    current = current.next
print(f"Size of linked list: {size}")
if __name__ == "__main__":
    pass
