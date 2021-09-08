import networkx as nx
import matplotlib.pyplot as plt

def ascend(partition):
    if partition == [0]: return [[1]]

    ascend_partition = [partition + [1]]
    unique_nums_in_partition = list(set(partition))

    index_to_increment = [
        partition.index(num)
        for num in unique_nums_in_partition
    ]

    for index in index_to_increment:
        new_partition = list(partition)
        new_partition[index] += 1
        ascend_partition.insert(0, new_partition)

    return ascend_partition

def partitions(n):
    result = [[n]]

    if n == 0 or n == 1: return result

    for index in range(1, n):
        for partition in partitions(n - index):
            partition_of_n = sorted([index] + partition, reverse = True)
            if partition_of_n not in result:
                result.append(partition_of_n)

    return result

def young_lattice(n):
    #Create an empty Graph
    G = nx.Graph()

    #Positions record the position of each node.
    positions = {}

    for order in range(0, n + 1):
        partitions_of_order = partitions(order)
        partitions_of_order.sort(key = len)

        #Get the length of the partition
        length = len(partitions_of_order)

        for p in partitions_of_order:
            #Add vertices on the Graph
            G.add_node(str(p))

            #Get the index of p at partition_of_order
            index_at_p = partitions_of_order.index(p)

            #Add position for each node
            positions[str(p)] = [- length / 2 + index_at_p + 1, order]

    #Add edges
    for order in range(0, n):
        for p in partitions(order):
            for adjacent_p in ascend(p):
                G.add_edge(str(p), str(adjacent_p))

    #Print out vertices
    v = list(G.nodes)
    print("Vertices of the Young Lattice graph of order %d: " % n)
    for index in range(0, len(v)):
        print("'" + v[index] + "'")

    print("*****************************************************************")

    #Print out edges
    e = list(G.edges)
    print("Edges of the Young Lattice graph of order %d: " % n)
    for index in range(0, len(e)):
        print(e[index])

    #Draw graph and display it
    nx.draw(G, with_labels = False, font_size = 12, pos = positions, node_size = 5)
    plt.show()

while(True):
    print("***************** Young Lattice Graph of Order N ****************")
    try:
        n = int(input("Enter N (To Quit, Press Enter): "))
    except ValueError:
        print("Good Bye!")
        print("*****************************************************************")
        break;
    print("*****************************************************************")
    young_lattice(n)
    print("*****************************************************************\n")
