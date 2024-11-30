#AHC003

class multi_gauss_dist_bayes:
    def __init__(self, N, m, mean, cov=[], R=1):
        self.N = N
        self.R = R
        self.m = m
        self.mu = np.array(mean)
        # ここに事前分布の共分散を書く。Ex make_cov関数の実装に基づいて共分散行列を生成
        self.sigma = cov

    def update_posterior_smw(self,y_new,c_new,R=None): # オンライン更新 [要修正] 高速化する
        """
        y_new: 新しく観測されたデータ（スカラー）
        c: 観測行列
        R: 観測ノイズの共分散行列
        siguma: 事前分布の共分散行列
        mu: 平均
        """
        y=y_new
        c=np.array(c_new).reshape((self.N,1))
        if R==None:
            vy=self.R
        else:
            vy=R
        vc=[0]*self.N
        vy+= c.T @ self.sigma @ c

        # 事後分布の平均を更新 μ = μ + 1/vy * V c (y - cT μ)
        self.mu = self.mu + 1 / vy * self.sigma @ c @ (y - c.T @ self.mu)
        np.clip(self.mu, 1/self.N/50, m)

        # 事後分布の共分散行列を更新 V = V - 1/vy * V c cT V
        self.sigma = self.sigma - 1 / vy * self.sigma @ c @ c.T @ self.sigma
        return # mu_post = mean, Sigma_post = V

    def update(self,target_area_set,res,R=None):
        c=[0]*self.N
        for x in target_area_set:
            c[x]=1
        k=len(target_area_set)
        obs_variance=(k*e*(1-e))**.5
        estimate=(k-res)*e+res*(1-e)
        self.update_posterior_smw(estimate,c,R=R)
