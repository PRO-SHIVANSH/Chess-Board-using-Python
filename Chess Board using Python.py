#Chess Board By Pro Shivansh :)
#Subscribe Pro Shivansh :) on YouTube
#Follow @pro_shivansh on Instagram
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

board=np.tile([1,0],[8,4])

for i in range(board.shape[0]):
	board[i]=np.roll(board[i],i%2)
	
cmap=ListedColormap(['#FFFFFF','#000000'])
plt.matshow(board,cmap=cmap,)
plt.xticks([])
plt.yticks([])
plt.show