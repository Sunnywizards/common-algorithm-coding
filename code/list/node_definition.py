class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def add(self, node):
        self.next = node


def create_link_list(val_list: list):
    if len(val_list) == 0:
        return
    head_node = Node(val_list[0])
    if len(val_list) > 1:
        tmp = head_node
        for val in val_list[1:]:
            tmp_node = Node(val)
            tmp.add(tmp_node)
            tmp = tmp.next
    return head_node


def print_link_list(head_node: Node):
    tmp = head_node
    print_list = []
    while tmp is not None:
        print_list.append(tmp.val)
        tmp = tmp.next
    print(print_list)
