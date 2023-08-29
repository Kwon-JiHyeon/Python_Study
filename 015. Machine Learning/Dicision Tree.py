from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class DecisionTreeClassification:
    def __init__(self):
        # Breast Cancer 데이터셋 가져오기 (출처: UCI ML Repository)
        uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
        self.df = pd.read_csv(uci_path, header=None)

        # 열 이름 지정
        self.df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
                          'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']

        pd.set_option('display.max_columns', 15)

    def prepare_data(self):
        # 데이터 전처리
        self.df['bare_nuclei'].replace('?', np.nan, inplace=True)
        self.df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)
        self.df['bare_nuclei'] = self.df['bare_nuclei'].astype('int')
        
        X = self.df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
                     'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]
        y = self.df['class']
        
        X = preprocessing.StandardScaler().fit(X).transform(X)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=10)
        
        return X_train, X_test, y_train, y_test

    def decision_tree_classification(self):
        # Decision Tree 분류
        X_train, X_test, y_train, y_test = self.prepare_data()
        tree_model = DecisionTreeClassifier(criterion='entropy', max_depth=5)
        tree_model.fit(X_train, y_train)
        y_hat = tree_model.predict(X_test)
        
        tree_matrix = metrics.confusion_matrix(y_test, y_hat)
        tree_report = metrics.classification_report(y_test, y_hat)
        
        print("Confusion Matrix:\n", tree_matrix)
        print("\nClassification Report:\n", tree_report)

# 클래스 인스턴스 생성
decision_tree_classification = DecisionTreeClassification()

# Decision Tree 분류 수행
decision_tree_classification.decision_tree_classification()
