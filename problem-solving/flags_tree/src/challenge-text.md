# What is the challenge
a tree is store in the file `tree.txt`, the tree is a binary tree where each node (except for the leaf nodes) has exactly two children, 
each child has a unique name (unique sequence of characters), the children of one node are separated by `,`, a space (` `) separates the children 
of each node of the current generation:

--------+
A       |
B,C     |
D,E F,G -- C children
-|------+
 | 
B children

Now given two nodes (node1, node2), let __n1__ = left_most(node1, node2) and __ni__ = right_most(node1, node2), and let __parent__ be the closest 
common ancestor to n1 and n2, and let the sequence s = (n1, n2, n3, ..., parent, ..., n(i-2), n(i-1), ni) be the sequence of nodes going from __n1__ to __ni__ 
through __parent__; the flag is INGENEER{initials(s)} where `initials(s)` is the concatenation of the nodes of the sequence.

