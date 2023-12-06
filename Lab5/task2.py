class node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = node(root_value)

    def insert(self, value):
        self.insert2(self.root, value)

    def insert2(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = node(value)
            else:
                self.insert2(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = node(value)
            else:
                self.insert2(current_node.right, value)

    def traverse(self):
        result = []
        self.traverse2(self.root, result)
        return result

    def traverse2(self, current_node, result):
        if current_node:
            self.traverse2(current_node.left, result)
            result.append(current_node.value)
            self.traverse2(current_node.right, result)


if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert(15)
    tree.insert(12)
    tree.insert(2)
    tree.insert(10)
    tree.insert(100)
    tree.insert(9)


    print("Tree Traversal:", tree.traverse())
