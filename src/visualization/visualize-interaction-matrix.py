import matplotlib.pyplot as plt 
import numpy as np 
import Graphics as artist

from matplotlib import cm

cmap = cm.get_cmap('bone_r',30)
cmap.set_bad('w')

drug_names = open('drug_names','r').read().splitlines()
interaction_matrix = np.load('small-interaction_matrix-2015-11-13.npy')
interaction_matrix[np.diag_indices_from(interaction_matrix)] /= 2
mask = np.triu(interaction_matrix)
masked = np.ma.array(interaction_matrix,mask=mask)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(masked,interpolation='nearest',aspect='auto', cmap=cmap)
artist.adjust_spines(ax)
cbar = plt.colorbar(cax)


a = plt.axes([.5, .65, .2, .2])
a.hist(np.tril(interaction_matrix).flat, color='k')
artist.adjust_spines(a)
plt.yscale('log', nonposy='clip')
plt.xscale('log')

plt.savefig('small-interaction_matrix-2015-11-13.tiff')
plt.savefig('small-interaction_matrix-2015-11-13.png')