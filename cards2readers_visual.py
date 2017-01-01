import matplotlib.pyplot as plt
import pylab
import numpy as np
import pandas as pd

#visual represenation of the data

cards_to_readers = pd.read_csv('PATH%\\CardIDs_to_readers.csv')
cards = cards_to_readers.iloc[:,0]
readers = cards_to_readers.iloc[:,1]

cnts = pd.read_csv('PATH%\\reader_counts_cardids.csv')
readers2 = cnts.iloc[:,0]
count = cnts.iloc[:,1]

plt.subplot(2,1,1)
plt.scatter(readers,cards)
plt.xlabel('reader')
plt.ylabel('cardID')
plt.xlim(0,max(readers)+1)
plt.grid(True)

plt.subplot(2,1,2)
plt.bar(readers2, count, align='center')
plt.xlabel('reader')
plt.ylabel('count of cardIDs')
plt.xlim(0,max(readers)+1)

#yticks = np.arange(0, max(readers)+1, 1)
#xticks = np.arange(0, max(cards)+1, 1)
#plt.xticks(xticks)
#plt.yticks(yticks)
plt.grid(True)
plt.show()
