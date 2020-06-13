import networkx as nx
import matplotlib.pyplot as plt

def ascend(p):
    if p == [0]: return [[1]]

    ascend_p = [p + [1]]
    ind_to_incr = []

    unique_num_in_p = list(set(p))

    for num in unique_num_in_p:
        get_index = p.index(num)
        ind_to_incr.append(get_index)

    for index in ind_to_incr:
        asc_p = list(p)
        asc_p[index] += 1
        ascend_p.insert(0, asc_p)

    return ascend_p

def partitions(n):
    result = [[n]]

    if n == 0 or n == 1: return result

    for index in range(1,n):
        for p in partitions(n - index):
            p_of_n = sorted([index] + p, reverse = True)
            if p_of_n not in result:
                result.append(p_of_n)

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
            positions[str(p)] = [-length / 2 + index_at_p + 1, order]

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
    nx.draw(G, with_labels = True, font_size = 12, pos = positions, node_size = 5)
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


