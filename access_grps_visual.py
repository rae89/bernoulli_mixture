import matplotlib.pyplot as plt
import pylab
import numpy as np
import pandas as pd

#plots data for visual representaiton of access groups

grps = pd.read_csv('PATH%\\AccessGroups_to_Readers.csv')
access = grps.iloc[:,0]
reader = grps.iloc[:,1]

cnts = pd.read_csv('PATH%\\accesgroup_cardid_cnts.csv')
access2 = cnts.iloc[:,0]
count = cnts.iloc[:,1]

plt.subplot(2,1,1)
plt.scatter(access,reader)
plt.xlabel('access group')
plt.ylabel('reader')
plt.xlim(0,max(grps.iloc[:,0])+1)
plt.grid(True)

plt.subplot(2,1,2)
plt.bar(access2, count, align='center')
plt.xlabel('access group')
plt.ylabel('count')
plt.xlim(0,max(grps.iloc[:,0])+1)

#yticks = np.arange(0, max(grps.iloc[:,1])+1, 1)
#xticks = np.arange(0, max(grps.iloc[:,0])+1, 1)
#plt.xticks(xticks)
#plt.yticks(yticks)
plt.grid(True)
plt.show()
