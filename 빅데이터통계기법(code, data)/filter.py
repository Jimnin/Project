import sys, os, glob, natsort
import pandas as pd

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법/사망자데이터')
file = glob.glob('*.csv')

col = ["지역","성별","날짜","나이","원인"]

for i in file:
    meta = pd.read_csv(i,encoding='CP949');meta.columns = col

    try:
        data = pd.concat([data,meta])
    except NameError:
        data = meta

fil = data[data['원인'] == 55][col[0:4]]

fil.to_csv("1997-2019자살.csv",encoding='CP949')
