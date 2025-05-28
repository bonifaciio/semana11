# 👷‍♂️ Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 🌲 BinarySearchTree base
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_rec(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_rec(current.right, value)

    def build_from_list(self, values):
        for val in values:
            self.insert(val)

# ✅ Challenge 2: 🧬 Find Lowest Common Ancestor
class BinarySearchTree(BinarySearchTree):  # 👀 Hereda de sí misma para extender
    def find_lca(self, val1, val2):
        """🧬 Find lowest common ancestor of two values in the BST"""
        current = self.root
        while current:
            if val1 < current.value and val2 < current.value:
                current = current.left  # 👈 Both left
            elif val1 > current.value and val2 > current.value:
                current = current.right  # 👉 Both right
            else:
                return current.value  # 🌟 Found LCA

# 🧪 Test cases
def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 1:", bst1.find_lca(2, 8) == 6)  # 🌲 Root is LCA

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 2:", bst2.find_lca(0, 4) == 2)  # 📚 Subtree LCA

    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 3:", bst3.find_lca(2, 3) == 2)  # 🔗 Ancestor node

    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("🧪 Test 4:", bst4.find_lca(5, 5) == 5)  # 🎯 Same node

    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 5:", bst5.find_lca(1, 3) == 2)  # 🌿 Leaf node LCA

# 🚀 Run all tests
test_find_lca()
