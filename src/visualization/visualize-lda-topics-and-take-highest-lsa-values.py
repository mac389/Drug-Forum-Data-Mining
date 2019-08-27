import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint 

from matplotlib import rcParams
rcParams['text.usetex'] = True

format = lambda text:r'\Large \textbf{%s}'%text

def parse(data):
	ans = {}
	for topic,values in enumerate(data):
		values = dict([item.split('*')[::-1] for item in values.split(' + ')])
		ans[topic] = values
	return ans

def adjust_spines(ax,spines=['bottom','left']):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward',10)) # outward by 10 points
            #spine.set_smart_bounds(True)
        else:
            spine.set_color('none') # don't draw spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        # no yaxis ticks
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])

def visualize_topics():

    data  = open('topics','rb').read().splitlines()

    topics = parse(data)
    all_words = list(set([item for sublist in topics.values() for item in sublist.keys()]))
    heatmap = np.zeros((15,len(all_words)))

    for i in range(15):
    	for j,word in enumerate(all_words):
    		heatmap[i][j] = float(topics[i][word]) if word in topics[i] else 0 

    fig = plt.figure(figsize=(8,10))
    ax = fig.add_subplot(111)
    cax = ax.imshow(heatmap.T,interpolation='nearest',aspect='auto',cmap=plt.cm.binary)
    ax.grid(True)
    adjust_spines(ax)

    ax.set_xticks(range(15))
    ax.set_xticklabels(map(format,map(str,range(15))))
    ax.set_xlabel(format('Topics'),rotation='horizontal')

    ax.set_yticks(range(len(all_words)))
    ax.set_yticklabels(map(lambda text:r'\textbf{\textsc{%s}}'%text,all_words),rotation='horizontal')


    plt.colorbar(cax)
    plt.tight_layout()
    plt.savefig('lsa_topics_visualized')
"""
def find_highest():
    data  = open('topics','rb').read().splitlines()
    topics = parse(data)
    all_words = list(set([item for sublist in topics.values() for item in sublist.keys()]))
    heatmap = np.zeros((100,len(all_words)))

    for i in range(100):
    	for j,word in enumerate(all_words):
         heatmap[i][j] = float(topics[i][word]) if word in topics[i] else 0 
         if heatmap[i][j] > 0.1:
             for key in topics[i].keys():
                 if topics[i][key]> 0.1:
                     print key
"""
def make_highest():
    fid = open('high_lsa_topics','w') 
    data  = open('topics','rb').read().splitlines()
    topics = parse(data)
    all_words = list(set([item for sublist in topics.values() for item in sublist.keys()]))
    heatmap = np.zeros((100,len(all_words)))

    for i in range(100):
        for j,word in enumerate(all_words):
            heatmap[i][j] = float(topics[i][word]) if word in topics[i] else 0 
            if heatmap[i][j] > 0.1:
                print word
                fid.write(word+ " ")
        fid.write("\n")
         
    fid.close()
    remove_excess_lines = []
    with open('high_lsa_topics','r') as fid:
        for line in fid:
            remove_excess_lines.append(line)
            remove_excess_lines = list(set(remove_excess_lines))
    with open('high_lsa_topics','w') as fid:
        for item in remove_excess_lines:
            fid.write(item)
            
make_highest()

#find_highest()