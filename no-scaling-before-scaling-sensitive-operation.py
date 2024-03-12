from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler # +

# Code source: Tyler Lanigan <tylerlanigan@gmail.com>
#              Sebastian Raschka <mail@sebastianraschka.com>
# License: BSD 3 clause

# Make a train/test split using 30% test size
RANDOM_STATE = 42
features, target = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.30, random_state=RANDOM_STATE
)

# Fit to data and predict using pipeline
# - clf = make_pipeline(PCA(n_components=2), GaussianNB())
clf = make_pipeline(StandardScaler(), PCA(n_components=2), GaussianNB()) # +
clf.fit(X_train, y_train)
pred_test = clf.predict(X_test)
ac = accuracy_score(y_test, pred_test)


### Scikit-Learn SVC
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline # +
from sklearn.preprocessing import StandardScaler # +

# Make a train/test split using 30% test size
RANDOM_STATE = 42
features, target = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.30, random_state=RANDOM_STATE
)

# Fit to data and predict using pipelined GNB and PCA
# - clf = SVC()
clf = make_pipeline(StandardScaler(), SVC()) # +
clf.fit(X_train, y_train)
pred_test = clf.predict(X_test)
ac = accuracy_score(y_test, pred_test)