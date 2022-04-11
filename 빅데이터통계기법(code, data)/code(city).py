import sys, os, glob, natsort # 데이터를 불러오기 위한 라이브러리
import pandas as pd # 데이터를 전처리하기 위한 라이브러리
from matplotlib import pyplot as plt # 그림을 그리기 위한 라이브러리
import numpy as np # 수학적인 계산 라이브러리
from matplotlib import font_manager, rc # 그림의 폰트를 지정해주는 라이브러리
from sklearn.preprocessing import MinMaxScaler # 데이터를 정규화하는 라이브러리
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering # 각각 거리기반, 밀도기반, 계층적 군집분석 라이브러리
from adjustText import adjust_text # 텍스트 겹침 방지 라이브러리
from scipy.cluster.hierarchy import dendrogram, linkage # 덴드로이드 라이브러리

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법')

data1 = pd.read_csv("count(locate).csv",encoding='CP949',index_col=[0])
data1 = data1.drop(data1.index[0]) ; del data1['세종'] ; col_1 = data1.columns

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법/실업자데이터')

data2 = pd.read_csv("count(locate).csv",encoding='CP949',index_col=[0]).transpose()
del data2['세종']

dt = pd.concat([data1,data2],axis=1)

normal = MinMaxScaler()
dt_scaled = pd.DataFrame(normal.fit_transform(dt.values),columns=[[*["자살자수"]*len(col_1),*["실업자수"]*len(col_1)]\
,[*col_1,*col_1]],index=dt.index)

ddt = dt_scaled['자살자수'].sum(); ddt1 = dt_scaled['실업자수'].sum()
dtdt = pd.concat([ddt,ddt1],axis=1);dtdt.columns = ["자살자수","실업자수"]

cluster = AgglomerativeClustering(n_clusters=4) # 군집분석 라이브러리를 바꿔가면서 분석
dtdt['cluster'] = cluster.fit_predict(dtdt) # KMeans, DBSCAN, AgglomerativeClustering
# 클러스터를 만들어서 군집 분류
fig,ax = plt.subplots(1,1,figsize=(10,8))

for city in col_1:
    plt.annotate(city,(dtdt['실업자수'].loc[city]+0.025,dtdt['자살자수'].loc[city]+0.025),fontsize=15)

for f in [0,1,2,3]: # 반복문을 돌면서 군집에 따라서 마커와 색깔 변경
    if f == 0:
        s = 'o'
    elif f == 1:
        s = 'X'
    elif f == 2:
        s = 'p'
    else:
        s = 's'
    plt.scatter(dtdt[dtdt['cluster'] == f]['실업자수'],dtdt[dtdt['cluster'] == f]['자살자수'],s=100,marker=s)

plt.xlabel("실업자수",fontsize=15);plt.ylabel("자살자수",fontsize=15,rotation=0,labelpad=20)
plt.setp(ax.get_xticklabels(),fontsize=15);plt.setp(ax.get_yticklabels(),fontsize=15)
plt.title("Hierarchical Method",fontsize=30)

plt.show()
