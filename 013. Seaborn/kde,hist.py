# kedpolt, histogram

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 그래프 객체 생성 (figure에 2개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# distplot 사라져서 주석처리
#sns.distplot(titanic['fare'], ax=ax1)

# kdeplot
sns.kdeplot(x='fare', data=titanic, ax=ax1)

# histplot
sns.histplot(x='fare', data=titanic, ax=ax2)

# 차트 제목 표시
# ax1.set_title('titanice fare - hist/ked')
ax1.set_title('titanice fare - ked')
ax2.set_title('titanice fare - hist')

plt.show()
