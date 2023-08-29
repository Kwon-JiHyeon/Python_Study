import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import metrics

class SVMClassification:
    def __init__(self):
        # 데이터 불러오기
        self.df = sns.load_dataset('titanic')
        pd.set_option('display.max_columns', 15)

    def prepare_data(self):
        # 데이터 전처리
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

    def svm_classification(self):
        # SVM 분류
        X_train, X_test, y_train, y_test = self.prepare_data()
        svm_model = SVC(kernel='rbf')
        svm_model.fit(X_train, y_train)
        y_hat = svm_model.predict(X_test)
        
        svm_matrix = metrics.confusion_matrix(y_test, y_hat)
        svm_report = metrics.classification_report(y_test, y_hat)
        
        print("Confusion Matrix:\n", svm_matrix)
        print("\nClassification Report:\n", svm_report)

# 클래스 인스턴스 생성
svm_classification = SVMClassification()

# SVM 분류 수행
svm_classification.svm_classification()
