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


def export_results(n, graph):
    f = open("graph_%d.dot" % n,"w+")
    f.write("digraph {\n")
    for key in graph:
        f.write("\t%d -> %d\n" % (key, graph[key]))
    f.write("}\n")


# initial conditions:
graph = {1:1, 2:1}
target = 2

while (True):
    target = target + 1
    n = target

    done = False
    while (not done):
        m = n
        if (n % 2) == 0:
            n = n / 2
        else:
            n = (n*3) + 1
        if (graph.has_key(n)):
            graph[m] = n
            done = True
    
    print(target, m)

    if (target % 1000) == 0:
        export_results(target, graph)
