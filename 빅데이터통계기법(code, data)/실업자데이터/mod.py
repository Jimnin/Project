import sys, os, glob, natsort
import pandas as pd
from datetime import datetime

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법/실업자데이터')

data = pd.read_csv("연령별 실업자.csv",encoding="CP949",index_col=1)
del data['성별'] ; data = data.transpose()
data.columns = ["20대","30대","40대","50대","60세이상"]
data.index = pd.period_range('2000-01-01','2020-01-01',freq='1Y')

data['연도'] = data.index.year

data = data[['연도','20대','30대','40대','50대','60세이상']]

data.to_csv("count(age).csv",encoding='CP949')
