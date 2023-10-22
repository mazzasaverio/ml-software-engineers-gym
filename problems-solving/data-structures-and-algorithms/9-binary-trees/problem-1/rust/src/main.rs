use std::time::Instant;

#[derive(Debug, PartialEq)]
struct TreeNode<T> {
    data: T,
    left: Option<Box<TreeNode<T>>>,
    right: Option<Box<TreeNode<T>>>,
}

fn is_symmetric<T: PartialEq>(tree: Option<Box<TreeNode<T>>>) -> bool {
    fn check_symmetric<T: PartialEq>(
        subtree_0: &Option<Box<TreeNode<T>>>,
        subtree_1: &Option<Box<TreeNode<T>>>,
    ) -> bool {
        match (subtree_0, subtree_1) {
            (None, None) => true,
            (Some(node0), Some(node1)) => {
                node0.data == node1.data
                    && check_symmetric(&node0.left, &node1.right)
                    && check_symmetric(&node0.right, &node1.left)
            }
            _ => false,
        }
    }
    tree.as_ref().map_or(true, |r| check_symmetric(&r.left, &r.right))
}

fn timing_decorator<F: Fn(Option<Box<TreeNode<i32>>>) -> bool>(n: usize, func: F) {
    let mut total_time = 0.0;
    for _ in 0..n {
        let start = Instant::now();
        // Create a symmetric tree for testing
        let root = Some(Box::new(TreeNode {
            data: 1,
            left: Some(Box::new(TreeNode {
                data: 2,
                left: Some(Box::new(TreeNode {
                    data: 3,
                    left: None,
                    right: None,
                })),
                right: Some(Box::new(TreeNode {
                    data: 4,
                    left: None,
                    right: None,
                })),
            })),
            right: Some(Box::new(TreeNode {
                data: 2,
                left: Some(Box::new(TreeNode {
                    data: 4,
                    left: None,
                    right: None,
                })),
                right: Some(Box::new(TreeNode {
                    data: 3,
                    left: None,
                    right: None,
                })),
            })),
        }));
        let _ = func(root);
        let duration = start.elapsed();
        total_time += duration.as_secs_f64();
    }
    println!(
        "\nFunction took {:.8} seconds to execute over {} runs.\n",
        total_time, n
    );
}

fn main() {
    timing_decorator(1_000_000, is_symmetric);
}
