def BellmanFord(graph,num_v,source=0):
    # graph = 隣接リスト g[source]=[(destination, dist),...]
    # edgeの初期化 edge = [(source,destination,dist),...]
    edges=[]
    for u in range(num_v):
        for v,d in graph[u]:
            edges.append((u,v,d))
    inf=float("inf")
    dist=[inf for i in range(num_v)]
    dist[source]=0
    neg=[False for i in range(num_v)]
    neg_flg=False
    
    #辺の緩和
    for i in range(num_v):
#       負閉路があっても、それを通ってスタートからゴールに辿り着けない場合は結果に影響しない事に注意！
#        if i==num_v-1:
#            check=dist[n-1]
        for u,v,d in edges:
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                if i==num_v-1:# and neg[v]==True:
                    # N回目で更新があったという事は負閉路が存在する
                    neg_flg=True
                neg[v] = True
    return neg_flg,dist
