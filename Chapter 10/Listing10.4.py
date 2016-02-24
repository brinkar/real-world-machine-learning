# Listing 10.4

from sklearn.neighbors import NearestNeighbors

weightFunctions = {
    'f1': lambda x: [1 for i in range(len(x))],   # equal weights
    'f2': lambda x: 1 / x,                        # 1 / dist
    'f3': lambda x: 1 / x ** 2                    # 1 / dist dist squared
}

# for each of the three weighting schemes compute predicted target
# values for K = 1 through 20

for idx, f in enumerate(weightFunctions):
    rmseL = []
    wf = weightFunctions[f]
    for nNeighbors in range(1,20, 1):
        neigh = NearestNeighbors(nNeighbors)    # initialize
        # VT is user / item transposed of the training set
        neigh.fit(VT)                           # find K nearest neighbors
        act = pd.Series()
        pred= pd.Series()
        # TT is user / item transpose of the test set 
        for i in range(TT.shape[0]):
            d = neigh.kneighbors(tt[i,:], return_distance=True)
            W = pd.Series([v for v in d[0][0]])
            y = pd.Series(pubsums.iloc[d[1][0]].CTR)
            act.append(pd.Series(tsums.iloc[i].CTR))
pred.append(pd.Series(np.average(y, weights = wf(W))))
    mse = act.sub(pred).pow(2).mean() / (pred.max() - pred.min())
    mseL.append(rmse)
    plt.subplot(130+idx+1)
    plt.plot(range(1,20,1), mseL)
    plt.tight_layout(pad=2.0)
