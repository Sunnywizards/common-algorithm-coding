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


# 1. Use stack to implement reversion
def reverse_list(head_node: Node):
    if head_node is None or head_node.next is None:
        return head_node
    node_list = []
    tmp = head_node
    while tmp is not None:
        node_list.append(tmp)
        tmp = tmp.next
    tmp = node_list[-1]
    rev_head = node_list.pop()
    while len(node_list) > 0:
        tmp_node = node_list.pop()
        tmp.next = tmp_node
        tmp = tmp.next
    tmp.next = None
    return rev_head


# 2. Iteration method
def reverse_list2(head_node: Node):
    if head_node is None or head_node.next is None:
        return head_node
    pre, cur = None, head_node

    while cur is not None:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node

    return pre


# 3. Recursive way
def reverse_list3(head_node: Node):
    if head_node is None or head_node.next is None:
        return head_node

    p = reverse_list3(head_node.next)
    head_node.next.next = head_node
    head_node.next = None

    return p


if __name__ == "__main__":
    value_list = [20, 30, 58, "sunny", True, "python"]
    head = create_link_list(value_list)
    print_link_list(head)
    # reverse_head1 = reverse_list(head)
    # reverse_head2 = reverse_list2(head)
    reverse_head3 = reverse_list3(head)
    # print_link_list(reverse_head1)
    # print_link_list(head)
    # print_link_list(reverse_head2)
    print_link_list(reverse_head3)
