# we can speed up traversal by performing the not in lin search in a set, which as you know is a hash look up (O(1))
def main(g, s):

    visited = []
    Q = [s]
    visited.append(Q[0])

    while len(Q) > 0:
        dq = Q.pop(0)

        print("dq:", dq)

        for i in range(0, len(g)):
            if g[dq][i] == 1 and i not in visited:
                Q.append(i)
                visited.append(i)


    print(visited)

print(main([
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0],
    [0,1,0,1,0,0,0,0],
    [0,1,1,0,1,1,0,0],
    [0,1,0,1,0,1,0,0],
    [0,0,0,1,1,0,1,1],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0]], 5))