import json

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string 
back into the tree.

For example, given the following Node class
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(root) -> str:
    serialized = dict()

    serialized["val"] = root.val
    serialized["left"] = serialize(root.left) if root.left != None else None
    serialized["right"] = serialize(root.right) if root.right != None else None

    return json.dumps(serialized)

def deserialize(s) -> Node:
    deserialized_json = json.loads(s)

    node_left = deserialize(deserialized_json["left"]) if deserialized_json["left"] != None else None
    node_right = deserialize(deserialized_json["right"]) if deserialized_json["right"] != None else None
    node = Node(deserialized_json["val"], node_left, node_right)

    return node

assert deserialize(serialize(node)).left.left.val == 'left.left'

"""
BONUS: This attempt does not use JSON but instead creates a printable String 
representation which can then be converted back to the Node class
"""
def bonus_serialize(root) -> str:
    """
    we begin by appending the class name and root value of the Node.
    """
    serialized = f"Node({root.val}, "
    while True:
        """
        we check if the left branch exists, and if it does we use recursion 
        to go down the branch. if not, we append None instead to later aid 
        us with the deserialization. we loop through this process until all 
        branches are serialized.
        """
        if root.left != None:
            serialized += f"{serialize(root.left)}, "
        else:
            serialized += "None, "

        """
        we do the same for the right branch
        """
        if root.right != None:
            serialized += serialize(root.right)
        else:
            serialized += "None"

        break
    """
    we close the Node and return the final string.
    """
    serialized += ")"
    return serialized

"""
a function which looks for parentheses pairs and then returns a sorted list 
of tupils and the indexes of each pair.
"""
def find_parens(s):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            toret[pstack.pop()] = i

    return sorted(list(toret.items()))

def bonus_deserialize(s) -> Node:
    """
    get the index of each parantheses in pairs, we will use this to seperate 
    the right and left branches 
    """
    found_peren_list = find_parens(s)
    """
    since the tupils are ordered, the first tupil is the root of the binary 
    tree. We thus use those indecies to slice the string
    """
    node = Node(s[found_peren_list[0][0]+1:found_peren_list[0][1]].split(", ")[0])
    left = []
    right = []
    is_left = True
    """
    we remove 1 from the usual range so that we may add 1 to the index to 
    compare the current and next index and whether the closing paren is less
    or greater than to the one after.
    
    as soon as the paren at index <index> is less than the one at index 
    <index + 1>, we know the next set of tupils represent the right branch.
    """
    for index in range(len(found_peren_list)-1):
        if found_peren_list[index][1] < found_peren_list[index+1][1]:
            is_left = False

        if is_left:
            left.append(found_peren_list[index +1])
        else:
            right.append(found_peren_list[index +1])
    
    """
    we use the first tupil in the list and pass it into the desserialize 
    method. we can do this as the first element in each list is the root 
    of each branch.
    """
    if len(left) != 0:
        node.left = deserialize(s[left[0][0]:left[0][1]+1])
    if len(right) != 0:
        node.right = deserialize(s[right[0][0]:right[0][1]+1])

    return node

