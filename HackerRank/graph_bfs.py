# Enter your code here. Read input from STDIN. Print output to STDOUT
def update(lvl, edges, node):
    lvl += 1
    ls = edges[node]
    lst_ret = [(lvl,i) for i in ls]
    return lst_ret
    
    
def main():
    edges = []
    e = []
    visited = {}
    level = 0
    T = int(raw_input())
    print T
    for num in range(T):
        N,M = [int(i) for i in raw_input().strip().split()]
        print M,N
        for i in range(N):
            edges.append([])
        for i in range(M):
            a,b = [int(i) for i in raw_input().strip().split()]
            e.append(a)
            e.append(b)
            edges[a].append(b)
            edges[b].append(a)
        print edges
        S = int(raw_input())
        print S
        que = [(level,S)]
        print que
        while(len(que) > 0):
            lvl,current = que.pop(0)
            que.extend(update(lvl, edges, S))
            if(current in visited.keys()):
                continue
            else:
                visited[current] = lvl*6
            print que
        k = visited.keys()
        ret = [visited[i] if i in k else -1 for i in e]
        print ' '.join(ret)

if __name__ == '__main__':
    main()
            
            
            
                
        
        
        
