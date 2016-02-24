# Listing 10.5

from sklearn.ensemble import RandomForestRegressor
from sklearn import cross_validation

# features are simple aggregates by pub
features = ['exposure', 'meanViewTime', 'nImps', 'reach', 'reachRate', 
                    'vImps', 'vRate', 'vReach', 'vReachRate']

# split data into test and train, features and targets
# train on 60% of the data, hold out 40% for test
X_train, X_test, y_train, y_test =  cross_validation.train_test_split(
              df[features], df.CTR, test_size=0.40, random_state=0)

# run the random forest regression with 100 trees; n_jobs parameter tells
# RF to use all available cores
reg = RandomForestRegressor(n_estimators=100, n_jobs=-1)
model = reg.fit(X_train, y_train)

# cross validation splits the training set to evalule the model
scores = cross_validation.cross_val_score(model, X_train, y_train)
print(scores, scores.mean())
 
# run the model on the test set
model.score(X_test, y_test)

plt.rcParams["figure.figsize"] = [12.0, 4.0]
plt.bar(range(len(features)), model.feature_importances_, align='center')
_ = plt.xticks(range(len(features)), features)
