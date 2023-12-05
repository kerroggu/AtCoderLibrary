def k_means(dusty_area,cluster_cnt=8,max_iter=10):
    global n,wall_r,wall_c,d,g
    vn=len(dusty_area)
    index=[i%cluster_cnt for i in range(vn)]
    random.shuffle(index)
    centroids=[0]*cluster_cnt
    
    for _ in range(max_iter):
        clusters=[[]for i in range(cluster_cnt)]
        for i in range(vn):
            clusters[index[i]]+=dusty_area[i],
        
        # 中心点の更新
        # 各クラスタのデータ点の平均をとる
        # O(m * n^2)
        for idx in range(cluster_cnt):
            min_dist=inf
            for alt in range(n*n):
                sum_dist=0
                for vt in clusters[idx]:
                    sum_dist+=dist[alt][vt]
                if min_dist>sum_dist:
                    min_dist=sum_dist
                    center=alt
            centroids[idx]=center
        
        # 所属クラスタの更新
        # 一番近い中心点のクラスタを所属クラスタに更新する
        new_clusters=[[]for i in range(cluster_cnt)]
        new_index=[0]*vn
        for point_idx in range(vn):
            cur_point=dusty_area[point_idx]
            min_dist=inf
            for cluster_idx in range(cluster_cnt):
                alt_dist=dist[centroids[cluster_idx]][cur_point]
                if min_dist>alt_dist:
                    min_dist=alt_dist
                    new_index[point_idx]=cluster_idx
            new_clusters[new_index[point_idx]]+=point_idx,
        
        # 空のクラスタがあった場合は中心点をランダムな点に割り当てなおす
        for i in range(cluster_cnt):
            if not new_clusters[i]:
                new_index[i]=RI(0,cluster_cnt-1)

        # 収束判定
        if index==new_index:
            break

        clusters = new_clusters
    return new_index
