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
    text = input()
    if "I" in (text):
        n = int(input())
        parents = list(map(int, input().split()))
        for i in range(n):
            if parents[i] < -1:
                return
            if parents[i] == -1:
                continue
            if i == parents[i]:
                return
        print(compute_height(n, parents))
    pass


sys.setrecursionlimit(10**7) 
threading.stack_size(2**27) 
threading.Thread(target=main).start()
