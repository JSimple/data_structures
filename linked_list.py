from node import Node

class LinkedList:
    
    def __init__(self, value = None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
    
    def insert_new_head(self, new_value):
        old_head = self.get_head_node()
        new_head = Node(new_value, old_head)
        self.head_node = new_head
    
    def stringify_list(self):
        str = ''
        current_node = self.head_node
        while current_node != None:
            str += current_node.get_value()
            current_node = current_node.get_next_node()
    
    def find_prev(self, val):
        current_node = self.head_node
        if current_node.get_value() == val:
            print('You entered the value of the head node!')
        while current_node.get_value() != None:
            if current_node.get_next_node().get_value == val:
                return current_node
            current_node = current_node.get_next_node()
        print('The value you entered is not in the list!')


    def swap_nodes(self, val1, val2):
        ## accomodate case where val 1 or 2 are head node
        val1_old_prev = self.find_prev(val1)
        val2_old_prev = self.find_prev(val2)
        val1_old_next = val1_old_prev.get_next_node().get_next_node()