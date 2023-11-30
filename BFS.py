from queue import Queue 
#깊이 우선 탐색(BFS)는 인접리스트로 구현, queue모듈의 Queue 클래스사용
def BFS_AL(vtx, aList, s):#aList는 인접리스트, s는 시작정점
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        print(vtx[s], end=' ')
        for v in aList[s] :
            if visited[v] == False:
                Q.put(v)
                visited[v] = True

#test
vtx = ['A','B','C','D','E','F','G','H']
alist = [[1,2],[0,3],...]
BFS_AL(vtx,aList,0)
