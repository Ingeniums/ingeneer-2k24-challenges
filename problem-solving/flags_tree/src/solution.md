# Solution
- After finding the two specified nodes, get the list of ancestry of the two nodes all the way up to the root node, using the fact that:
for a given pair with index n (n 1..N) the pair of its parent is (n div 2 + 1), its exact parent is either the first (n mod 2 == 1) or the second 
(n mod 2 == 2), traverse the tree upwards keeping track of the nodes, outputting the list of ancestry.

- Use the list of ancestry of the two nodes the determine the closest common ancestor.
- Remove unnecessary nodes.
- Determine the left most node (the left most node is the node having the left child of the common ancestor as an ancestor).
- Reverse the ancestry list of the left most node.
- combine the lists.
- get the initial characters of each node name.

