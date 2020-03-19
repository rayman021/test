# -*- codin`g: utf-8 -*-
"""
Created on Wed Feb 27 18:07:26 2019

@author: 13107
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import matplotlib.dates as mdate


#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)




df=pd.read_csv('bus_modify_direction0.csv',sep=',',header=0,skip_blank_lines=False, encoding='UTF-8')
group_list=[]
plt.figure(figsize=(12, 6))
for name, group in df.groupby('vehicle_id'):
    aa = pd.to_datetime(group.arrival_time)
    #t_time=[]
#    for t_a in group.arrival_time:
#        aa=time.localtime(t_a)
#        t_time.append(aa)
    #print(name)
    #print(group)
    plt.plot(aa,group.dis)
    #plt.plot(group.arrival_time, group.dis)

plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))    
#plt.plot(df.arrival_time, df.dis)
#plt.xlim(43466.2, 43467)
#plt.savefig('7.jpg',dpi=1000)
plt.show()
