import sys, os, glob, natsort
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법')

data = pd.read_csv("1997-2019데이터(자살)_1.csv",encoding='CP949',index_col=0)

bins = np.insert(np.append(np.arange(5,13 +2,2),19),0,0)
name = ["10대","20대","30대","40대","50대","60세이상"]
data['나이'] = pd.cut(data['나이'],bins,labels=name)

count_data = pd.pivot_table(data,index=["연도"],columns="지역",values="나이",aggfunc=["count"])

count_data.to_csv("count(locate).csv",encoding='CP949')
