# pairplot

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

titanic_pair = titanic[['age','pclass','fare']]

g = sns.pairplot(titanic_pair)
