class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    """Inserta un valor en el BST"""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def build_bst(values):
    """Construye un BST a partir de una lista de valores"""
    root = None
    for val in values:
        root = insert(root, val)
    return root

def range_query(root, min_val, max_val):
    """Encuentra todos los valores en el rango [min_val, max_val] usando recorrido inorder optimizado"""
    result = []
    
    def inorder(node):
        if not node:
            return
        if node.val > min_val:
            inorder(node.left)
        if min_val <= node.val <= max_val:
            result.append(node.val)
        if node.val < max_val:
            inorder(node.right)
    
    inorder(root)
    return result

# ✅ Test cases
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])       # 🎯 Normal range
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])              # 📊 Full coverage
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])                         # 📭 Empty result
print(range_query(build_bst([15]), 10, 20) == [15])                             # 🌱 Single node
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])     # 🔗 Include boundaries
