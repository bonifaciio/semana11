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

def find_lca(root, val1, val2):
    """Encuentra el ancestro común más bajo (LCA) en un BST"""
    while root:
        if val1 < root.val and val2 < root.val:
            root = root.left  # 👈 Ambos valores están en el subárbol izquierdo
        elif val1 > root.val and val2 > root.val:
            root = root.right  # 👉 Ambos valores están en el subárbol derecho
        else:
            return root.val  # 🎯 Este nodo es donde se separan los caminos
    return None  # Si no se encuentra LCA (no debería pasar si los valores existen)

# ✅ Test cases
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # 🌲 Root as LCA
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # 📊 Subtree LCA
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # 🔗 Ancestor relationship
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)                    # 🎯 Same node
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)        # 🌱 Leaf LCA
