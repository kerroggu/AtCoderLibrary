# Verified by
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ao
# edgeを引数に二部グラフ判定

def IsBipartite(edge):
    n=len(edge)
    v=[-1 for i in range(n)]
    for c in range(n):
        if v[c]!=-1:
            continue
        q=[c]
        v[c]=0
        while q:
            c=q.pop()
            for nb in edge[c]:
                if v[nb]==-1:
                    q.append(nb)
                    v[nb]=1-v[c]
                elif v[nb]==v[c]:
                    return False
    return True
