from ast import While
import queue


class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __iter__(self):
        if self.left: yield from self.left
        yield self
        if self.right: yield from self.right
    
    def subtree_first(self):
        if self.left: return self.left.subtree_first()
        else:         return self

    def subtree_last(self):
        if self.right: return self.right.subtree_last()
        else:          return self

    # Need to add parent attribute for this to work
    def successor(self):
        original = self
        if self.right: 
            return self.right.subtree_first()
        else:
            while self.parent and (self is self.parent.right):
                self = self.parent
            if self.parent:
                return self.parent
            else:
                return original

    def predecessor(self):
        original = self
        if self.left:
            return self.left.subtree_last()
        else:
            while self.parent and (self is self.parent.left):
                self = self.parent
            return self.parent if self.parent else original
    
    def subtree_insert_before(self,node):
        if not self.left:
            self.left = node
            node.parent = self
        else:
            self = self.left.subtree_last()
            self.right = node
            node.parent = self

    def subtree_insert_after(self,node):
        pass

    def subtree_delete(self):
        pass

if __name__ == '__main__':
    root = TreeNode(5, TreeNode(3,TreeNode(2),TreeNode(4)), TreeNode(7,TreeNode(6),TreeNode(9,TreeNode(8),TreeNode(10))))

    node_list = [x for x in root]

    node_list[0].parent = node_list[1]
    node_list[1].parent = node_list[3]
    node_list[2].parent = node_list[1]
    node_list[3].parent = None
    node_list[4].parent = node_list[5]
    node_list[5].parent = node_list[3]
    node_list[6].parent = node_list[7]
    node_list[7].parent = node_list[5]
    node_list[8].parent = node_list[7]

    # for node in node_list:
    #     print(f"Node: {node.val} Parent: {node.parent.val if node.parent else None}")

    # print(node_list[8].successor().val)
    
    print(node_list[6].val)
    print(node_list[6].predecessor().val)




    # for i, node in enumerate(node_list):
    #     print(i, node.val)

    # tree_start = root.subtree_first()
    # tree_last = root.subtree_last()
    # tree_succesor = root.successor()
    # # print(tree_start.val, tree_last.val)
    # # print(tree_succesor.val)
    # node3 = None
    # for r in root:
    #     if r.val == 3:
    #         node3 = r
    #         break
    

    # print(node3.val)