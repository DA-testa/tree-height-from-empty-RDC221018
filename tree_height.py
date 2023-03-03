# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    height = [0] * n

    def compute_node_height(node):
        if height[node] != 0:
            return height[node]

        if parents[node] == -1:
            height[node] = 1
        else:
            height[node] = 1 + compute_node_height(parents[node])

        return height[node]

    for i in range(n):
        compute_node_height(i)

    return max(height)


def main():
    # implement input form keyboard and from files
    n = int(input())
    parents = list(map(int,input().split()))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    for i in range(n):
        if parents[i] < -1:
            return

        if parents[i] == -1:
            continue

        if i == parents[i]:
            return
    
    print(compute_height(n, parents))
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))