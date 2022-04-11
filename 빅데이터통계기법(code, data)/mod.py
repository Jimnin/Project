import sys, os, glob, natsort
import pandas as pd
from datetime import datetime

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법')

data = pd.read_csv("1997-2019데이터(자살).csv",encoding="CP949",index_col=0)

date = pd.to_datetime(data['날짜'],format='%Y%m%d')
data['연도'] = date.dt.year ; data['분기'] = date.dt.quarter
data = data.drop(['날짜'],axis=1)

data = data[['연도','분기','지역','성별','나이']]

data.to_csv("1997-2019데이터(자살)_1.csv",encoding='CP949')
