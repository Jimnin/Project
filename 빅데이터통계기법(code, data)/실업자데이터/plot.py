import sys, os, glob, natsort
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

os.chdir('C:/Users/hjm01/Desktop/대학원/빅데이터통계기법/실업자데이터')

data = pd.read_csv("count(age).csv",encoding='CP949',index_col=[0,1])

fig,ax = plt.subplots(figsize=(10,7))
data[['20대','30대','40대']].plot(ax=ax)
plt.xticks(fontsize=15) ; plt.yticks(fontsize=15)
plt.xlabel("날짜",fontsize=15) ; plt.ylabel("(천명)",fontsize=15,rotation=0,labelpad=25)
leg = plt.legend(fontsize=15) ; leg_line = leg.get_lines() ; plt.setp(leg_line, linewidth=3)
plt.show()
