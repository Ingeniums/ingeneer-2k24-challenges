import random

class TreeNode:
    def __init__(self, parent, left, right, name) -> None:
        self.parent = parent
        self.left = left
        self.right = right
        self.name = name
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return f"{self.name} (left: {self.left}, right: {self.right})"

tree_array = []
def load_tree_array(text_lines, index = 0):
    global tree_array
    if text_lines[index] == "":
        return
    tree_array.append([])
    child_index = 0
    for children in text_lines[index].split(" "):
        parent = None if len(tree_array) == 1 else tree_array[index - 1][child_index] 
        children = list(map(lambda name: TreeNode(parent, None, None, name), children.split(",")))
        if len(tree_array) != 1:
            try:
                parent.left = children[0]
                parent.right = children[1]
            except Exception:
                raise Exception("hello there")
        tree_array[index].extend(children)
        child_index += 1
    load_tree_array(text_lines, index + 1)

def get_random_child(node):
    return node.left if random.randint(0, 1) == 0 else node.right

def get_root(tree_array):
    return tree_array[0][0]

def get_random_common_parent(depth, root, level = 1):
    if depth == level:
        return root
    return get_random_common_parent(depth, get_random_child(root), level + 1)

def get_char(node):
    return str(node)[0]

def gen_key(length, parent, level = 1, place_before = None):
    if parent.left == None or parent.right == None:
        extremeties.append(parent)
        return get_char(parent)
    if length == 1:
        extremeties.append(parent)
        return get_char(parent)
    if level == 1:
        path.extend([parent.left, parent, parent.right])
        return f"{gen_key(length - 2, parent.left, level + 1, True)}{get_char(parent)}{gen_key(length - 2, parent.right, level + 1, False)}"
    if place_before:
        child = get_random_child(parent)
        path.insert(0, child)
        return f"{gen_key(length - 2, child, level + 1, True)}{get_char(parent)}"
    child = get_random_child(parent)
    path.append(child)
    return f"{get_char(parent)}{gen_key(length - 2, child, level + 1, False)}"

num_rounds = 20
pairs = []
keys = []
paths = []
for i in range(num_rounds):
    extremeties = []
    path = []
    tree_array = []
    print(f"generating key of tree {i}")
    with open(f"./files/tree_{i}.txt", "r") as tree:
        load_tree_array(tree.read().split("\n"))
        # randomize for more randomness
        parent_depth = 9
        original_key_length = 21 
        key_length = 0
        make_even = False
        if original_key_length % 2 == 0:
            make_even = True
            key_length += 1
        else:
            key_length = original_key_length
    
        max_depth = 20
        if (key_length - 1) // 2 + parent_depth >= max_depth:
            raise ValueError(f"invalid key length for specified parent_depth, for key_length = {original_key_length} parent_depth < {max_depth - ((key_length - 1) // 2)}")
        key = gen_key(key_length, get_random_common_parent(parent_depth, get_root(tree_array)))
        if make_even:
            remove_start = random.randint(0, 1) == 0
            if remove_start:
                key = key[1:]
            else:
                key = key[:len(key) - 1]
        pairs.append(extremeties)
        paths.append(" -> ".join([str(node) for node in path]))
        keys.append(f"INGENEER{{{key}}}")

with open("./files/ends.txt", "w") as pairs_file:
    pairs_file.write("\n".join([f"{pair[0]} -> {pair[1]}" for pair in pairs]))
with open("flag.txt", "w") as flag:
    flag.write("\n".join(keys))
with open("paths.txt", "w") as paths_file:
    paths_file.write("\n".join(paths))
