# Young Lattice Generator

<p align = 'justify'>
The Young lattice or Young graph is an infinite ranked graph (with one rank or level for each natural number n) constructed as follows.
For each natural number n, the vertices at level n are precisely the partitions of n. We draw an edge connecting a partition of n and
a partition of n + 1 if the Young diagram (also called Ferrers diagram) for the partition of n + 1 can be obtained by inserting one block
into the Young diagram of the partition of n. In algebraic terms, this means that the partition of n + 1 is obtained from the partition
of n either by incrementing one of the parts by 1 or by adding a new part with value 1. (source) https://groupprops.subwiki.org/wiki/Young_lattice
</p>

<p align = 'justify'>
Since we cannot construct the Young graph with infinitely many nodes, this python program creates the subgraph of the Young graph where
the vertices of the subgraph are all partitions of 1, 2, up till N.
</p>

---
### How to run the script?

<p align = 'justify'>
Before running the python script, make sure you have networkx and matplotlib in python library. If you do have then for MACs,
</p>

 * open terminal,
 * go to the directory where the python script is located,
 * then type python3 young_lattice.py,
---

### Example Graphs

Here is the subgraph for N = 3
<p align="center">
  <img src="https://github.com/xnell90/Miscellaneous-Projects/blob/master/Young_Lattice_Generator/Young%20Lattice%20of%20Order%203.png"/>
</p>

Here is another subgraph for N = 4
<p align="center">
  <img src="https://github.com/xnell90/Miscellaneous-Projects/blob/master/Young_Lattice_Generator/Young%20Lattice%20of%20Order%204.png"/>
</p>
