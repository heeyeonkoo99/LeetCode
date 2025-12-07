
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1  # postorder의 마지막 인덱스부터 시작

        def helper(left, right):
            if left > right:
                return None

            # postorder에서 root 꺼내기
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            # inorder에서 root 위치 찾기
            mid = inorder_map[root_val]

            # **오른쪽 먼저 재귀**, 그 다음 왼쪽
            root.right = helper(mid + 1, right)
            root.left = helper(left, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
