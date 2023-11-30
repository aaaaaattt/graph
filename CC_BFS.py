from queue import Queue

#연결 성분 검사 주 함수
def find_connected_component(vtx, adj) :
    n = len(vtx)
    visited = [False]*n
    groups = [] #연결 성분 리스트
    for v in range(n) :
        if visited[v] == False :
            color = bfs_cc(vtx, adj, v, visited)
            groups.append(color)
    return groups

#너비우선탐색을 이용한 연결 성분 검사
#그래프는 인접행렬로 표현
def bfs_cc(vtx, adj, s, visited):
    group = [s]
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s=Q.get()
        for v in range(len(vtx)) :
            if visited[v] == False and adj[s][v] != 0:
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group

