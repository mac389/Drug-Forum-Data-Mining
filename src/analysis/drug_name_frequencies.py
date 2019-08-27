from collections import Counter

import matplotlib.pyplot as plt 
import Graphics as artist 

from matplotlib import rcParams
rcParams['text.usetex'] = True

drug_names = open('drug_names','r').read().splitlines()
drug_name_frequencies = Counter(drug_names)

cutoff=20
name, frequency = zip(*drug_name_frequencies.most_common(cutoff))
idx = range(len(frequency))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(idx,frequency, color='k')

artist.adjust_spines(ax)
ax.set_ylabel(artist.format('No. of mentions'))
ax.set_xticks(range(len(name)))
ax.set_xticklabels(map(artist.format,name), rotation=90)

a = plt.axes([.65, .6, .2, .2])
_,full_frequencies = zip(*drug_name_frequencies.most_common())
a.hist(full_frequencies, color='k')
artist.adjust_spines(a)
a.set_xlabel(artist.format('No. of mentions'))
a.set_ylabel(artist.format('No. of substances'))
plt.yscale('log', nonposy='clip')
for label in a.get_xticklabels()[1::2]:
    label.set_visible(False)
plt.tight_layout()
plt.savefig('drug-name-frequency.png')