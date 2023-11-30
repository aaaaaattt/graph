def DFS(vtx,adj, s, visited) :
    print(vtx[s],end=' ')
    visited[s] = True

    for v in range(len(vtx)) :
        if adj[s][v] != 0 :
            if visited[v] == False:
                DFS(vtx, adj, v,visited)