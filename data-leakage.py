from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.pipeline import make_pipeline # +

n_samples, n_features, n_classes = 200, 10000, 2
rng = np.random.RandomState(42)
X = rng.standard_normal((n_samples, n_features))
y = rng.choice(n_classes, n_samples)

# - X_selected = SelectKBest(k=25).fit_transform(X, y)
# - X_train, X_test, y_train, y_test = train_test_split(X_selected, y, random_state=42)
# - gbc = GradientBoostingClassifier(random_state=1)
# - gbc.fit(X_train, y_train)
# - y_pred = gbc.predict(X_test)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42) # +
pipeline = make_pipeline(SelectKBest(k=25), GradientBoostingClassifier(random_state=1)) # +
pipeline.fit(X_train, y_train)# +
y_pred = pipeline.predict(X_test)# +

accuracy_score(y_test, y_pred)