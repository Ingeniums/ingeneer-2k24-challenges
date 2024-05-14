import random
import os

name_length = 5
tree_depth = 17 
names_count = sum([2 ** i for i in range(tree_depth)])
char_set = "azertyuiopqqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN123456789_"

names = []
def gen_names(length, current_length = 0, chars = ""):
    if current_length == length:
        c = list(chars)
        random.shuffle(c)
        names.append("".join(c))
        return
    for char in char_set:
        if len(names) == names_count:
            return
        gen_names(length, current_length + 1, chars + char)
    pass

def gen_tree(depth, name_length, level = 1):
    global name_id
    if depth < level:
        return ""
    result = ""
    for i in range(2 ** (level - 1)):
        result += names[name_id] + ("," if i % 2 == 0 else " ")
        name_id += 1
    result = result[:len(result) - 1] + "\n"
    return result + gen_tree(depth, name_length, level + 1)

if not os.path.exists("./files"):
    os.makedirs("./files")


num_rounds = 20
for i in range(num_rounds):
    print(f"generating tree_{i}.txt")
    with open(f"./files/tree_{i}.txt", "w") as tree:
        gen_names(name_length)
        random.shuffle(names)
        name_id = 0
        tree.write(gen_tree(tree_depth, name_length))
        names = []
