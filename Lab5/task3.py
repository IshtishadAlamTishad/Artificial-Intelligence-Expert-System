from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    def insert(self, value):
        self._insert_recursive(self.root, value)
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
    def search(self, value):
        return self._search_recursive(self.root, value)
    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)
    def bfs_search(self, target):
        if self.root is None:
            return None

        queue = deque()
        queue.append(self.root)

        while queue:
            current_node = queue.popleft()
            if current_node.value == target:
                return current_node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    def traverse(self):
        result = []
        self._traverse_recursive(self.root, result)
        return result

    def _traverse_recursive(self, current_node, result):
        if current_node:
            self._traverse_recursive(current_node.left, result)
            result.append(current_node.value)
            self._traverse_recursive(current_node.right, result)

if __name__ == "__main__":
    root_value = 10
    tree = BinaryTree(root_value)
    tree.insert("RED")
    tree.insert("GREEN")
    tree.insert("YELLOW")
    tree.insert("VIOLET")
    #tree.insert(100)
    #tree.insert(9)

    print("Tree Search for 100:", tree.search("RED"))
    print("Tree Search for 8:", tree.search("MAGENTA"))


    print("Tree Traversal:", tree.traverse())
