from functools import wraps
import time


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def timing_decorator(n=1000):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0.0
            start_time = time.time()
            for _ in range(n):
                result = func(*args, **kwargs)
            end_time = time.time()
            total_time += end_time - start_time
            print(
                f"\nFunction {func.__name__} took of {total_time:.8f} seconds to execute over {n} runs.\n"
            )
            return result

        return wrapper

    return actual_decorator


@timing_decorator(n=1000000)
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
        return False

    return not tree or check_symmetric(tree.left, tree.right)


# Create a symmetric tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

# Test the decorated function
is_symmetric_result = is_symmetric(root)
is_symmetric_result
