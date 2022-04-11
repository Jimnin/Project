import sys, os, glob, natsort
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from sklearn.preprocessing import MinMaxScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
from adjustText import adjust_text

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

col_1 = ["20대","30대","40대","50대"]
os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법')

data1 = pd.read_csv("count(age).csv",encoding='CP949',index_col=[0])[col_1]

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법/실업자데이터')

data2 = pd.read_csv("count(age).csv",encoding='CP949',index_col=[0])[col_1]

dt = pd.concat([data1,data2],axis=1)

normal = MinMaxScaler()
dt_scaled = pd.DataFrame(normal.fit_transform(dt.values),columns=[[*["자살자수"]*len(col_1),*["실업자수"]*len(col_1)],[*col_1,*col_1]],index=dt.index)

fig,ax = plt.subplots(2,2,figsize=(12,8))
ax_list = [(0,0),(0,1),(1,0),(1,1)]

for col,xy in zip(col_1,ax_list):
    ax[xy].scatter(dt_scaled['실업자수'][col],dt_scaled['자살자수'][col],s=1,color="black")
    ax[xy].set_xlim(-0.05,1.05);ax[xy].set_ylim(-0.05,1.05)
    texts = []
    for num,year in enumerate(dt_scaled.index):
        tx = ax[xy].annotate(year,(dt_scaled['실업자수'][col][year],dt_scaled['자살자수'][col][year]))
        texts.append(tx)
    adjust_text(texts,ax=ax[xy])
plt.subplots_adjust(hspace=0,wspace=0)
for z in [(0,1),(1,1)]:
    ax[z].set_yticklabels([],visible=False)

poly_features = PolynomialFeatures(degree=4,include_bias=False) # 다항회귀 실시
linear_features = PolynomialFeatures(degree=1,include_bias=False) # degree=1인 경우 1인 선형회귀
ddt = (dt_scaled.dropna(axis=0)).drop(index=[2000,2001]) # 2000,2001년 데이터 제외

for age,aax in zip(col_1,ax_list):
    X = np.array(ddt['실업자수'][age])

    X_poly = poly_features.fit_transform(X.reshape(-1,1)) # 다항회귀 실시
    X_poly_1 = linear_features.fit_transform(X.reshape(-1,1)) # 선형회귀 실시
    y = ddt['자살자수'][age]
    lin_reg = LinearRegression();lin_reg_1 = LinearRegression() # 선형회귀 라이브러리를 이용하여 계수를 얻기
    lin_reg.fit(X_poly,y)
    lin_reg_1.fit(X_poly_1,y)

    X_new = np.linspace(0,1,100).reshape(-1,1)
    X_new_poly = poly_features.transform(X_new)
    X_new_poly_1 = linear_features.transform(X_new)
    y_new = lin_reg.predict(X_new_poly) # 다항회귀 예측
    y_new_1 = lin_reg_1.predict(X_new_poly_1) # 선형회귀 예측
    ax[aax].plot(X_new,y_new,'r--',label="4-degree") # 4차 다항회귀 선
    ax[aax].plot(X_new,y_new_1,'b--',label="1-degree") # 1차 선형회귀 선
    plt.setp(ax[aax].get_xticklabels(),fontsize=15)
    plt.setp(ax[aax].get_yticklabels(),fontsize=15)
    leg = ax[aax].legend()
    leg.set_title(str(age),prop={'weight':'heavy'})

plt.show()
