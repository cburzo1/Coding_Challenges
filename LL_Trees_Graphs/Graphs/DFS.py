def main(mx, s):
    stk = [s]
    visited = []

    while stk:
        u = stk.pop()
        if u not in visited:
            visited.append(u)
            # Push neighbors in reverse for left-to-right DFS
            for i in reversed(range(len(mx[u]))):
                if mx[u][i] == 1 and i not in visited:
                    stk.append(i)
    return visited


print(main([
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,0],
    [0,1,0,1,0,0,0,0],
    [0,1,1,0,1,1,0,0],
    [0,1,0,1,0,1,0,0],
    [0,0,0,1,1,0,1,1],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0]], 1))