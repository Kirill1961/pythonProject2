from catboost import CatBoostClassifier
import catboost

cat_features = [0,1,2]

train_data = [["a", "b", 1, 4, 5, 6],
["a", "b", 4, 5, 6, 7],
["c", "d", 30, 40, 50, 60]]

train_labels = [1,1,0]

model = CatBoostClassifier(iterations=20,
loss_function = "CrossEntropy",
train_dir = "crossentropy")

model.fit(train_data, train_labels, cat_features)
predictions = model.predict(train_data)

# TODO для jupiter
# w = catboost.MetricVisualizer('/crossentropy/')
# w.start()