#------------------------------------------------------------------------------
# Hailstone path graph calculator
# CAH 2019-12-26
#
# - The 'hailstone path' for a given number N is calculated as follows:
#    - if N is odd, multiply by 3 and add 1
#    - if N is even, divide by 2
#    - Iterate until the result is 1
# - The graph outputs each number, and has a directed line to its "next" neighbor
#
#------------------------------------------------------------------------------

import os

def export_results(n, graph):
    f = open("out/graph_%d.dot" % n,"w+")
    f.write("digraph {\n")
    for key in graph:
        f.write("\t%d -> %d\n" % (key, graph[key][0]))
    f.write("}\n")


# graph:  { number: (next, total_num_iter) }
graph = {1: (1, 0) }

target = 2
max_iter = 0

if not os.path.exists("out"):
    os.makedirs("out")

while (True):
    target = target + 1
    n = target
    num_iter = 0

    done = False
    while (not done):
        m = n
        num_iter = num_iter + 1
        if (n % 2) == 0:
            n = n / 2
        else:
            n = (n*3) + 1
        if (graph.has_key(n)):
            graph[m] = (n, 1 + graph[n][1])
            done = True
            num_iter = num_iter + graph[n][1]
            if ( num_iter > max_iter):
                max_iter = num_iter
                print("%d: %d" % (target, max_iter) )

