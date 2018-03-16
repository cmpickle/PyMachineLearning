from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]] # weight and 1 for smooth and 0 for bumpy
labels = ["apple", "apple", "orange", "orange"] # 0 for apple and 1 for orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150, 1]]))