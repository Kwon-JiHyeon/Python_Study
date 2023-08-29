import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

class KNNClassification:
    def __init__(self):
        # 데이터 불러오기
        self.df = sns.load_dataset('titanic')
        pd.set_option('display.max_columns', 15)

    def prepare_data(self):
        # NaN값 처리 및 원핫인코딩
        rdf = self.df.drop(['deck', 'embark_town'], axis=1)
        rdf = rdf.dropna(subset=['age'], how='any', axis=0)
        most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
        rdf['embarked'].fillna(most_freq, inplace=True)

        ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
        onehot_sex = pd.get_dummies(ndf['sex'])
        ndf = pd.concat([ndf, onehot_sex], axis=1)
        onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
        ndf = pd.concat([ndf, onehot_embarked], axis=1)
        ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
        
        X = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']]
        y = ndf['survived']
        
        X = StandardScaler().fit(X).transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
        
        return X_train, X_test, y_train, y_test

    def knn_classification(self):
        # KNN 분류
        X_train, X_test, y_train, y_test = self.prepare_data()
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(X_train, y_train)
        y_hat = knn.predict(X_test)
        
        knn_matrix = metrics.confusion_matrix(y_test, y_hat)
        knn_report = metrics.classification_report(y_test, y_hat)
        
        print("Confusion Matrix:\n", knn_matrix)
        print("\nClassification Report:\n", knn_report)

# 클래스 인스턴스 생성
knn_classification = KNNClassification()

# KNN 분류 수행
knn_classification.knn_classification()
