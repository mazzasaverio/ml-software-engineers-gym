class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def tree_traversal(root):
    if root:
        # Preorder: Processes the root before the traversals of left and right children.
        print("Preorder: %d" % root.data)
        tree_traversal(root.left)
        # Inorder: Processes the root after the traversal of left child and before the traversal of right child.
        print("Inorder: %d" % root.data)
        tree_traversal(root.right)
        # Postorder: Processes the root after the traversals of left and right children.
        print("Postorder: %d" % root.data)


import collections


def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        "BalancedStatusWithHeight", ("balanced", "height")
    )

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced_binary_tree = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced_binary_tree, height)

    return check_balanced(tree).balanced


def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (
                subtree_0.data == subtree_1.data
                and check_symmetric(subtree_0.left, subtree_1.right)
                and check_symmetric(subtree_0.right, subtree_1.left)
            )
        # One subtree is empty, and the other is not.
        return False

    return not tree or check_symmetric(tree.left, tree.right)


import heapq
import itertools

def top_k(k, stream):
    # Entries are compared by their lengths.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        # Push next_string and pop the shortest string in min_heap.
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]