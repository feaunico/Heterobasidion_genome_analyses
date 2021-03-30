

import matplotlib
matplotlib.use('Agg')
from matplotlib.patches import Polygon

import numpy as np
import matplotlib.pyplot as plt




ccs = []
with open("5313_ccs.fastq") as infile:
    for line in infile:
        if line[0] in ['A','C','G','T','N']:
            ccs.append(len(line))
print len(ccs), np.median(ccs), np.mean(ccs), np.std(ccs), max(ccs), min(ccs)
long = []

with open("5313_long.fastq") as infile:
    for line in infile:
        if line[0] in ['A','C','G','T','N']:
            long.append(len(line))
print 'done 1'
print len(long), np.median(long), np.mean(long), np.std(long), max(long), min(long)
sub = []

with open("5313_sub.fastq") as infile:
    for line in infile:
        if line[0] in ['A','C','G','T','N']:
            sub.append(len(line))
print 'done 2'
print len(sub), np.median(sub), np.mean(sub), np.std(sub), max(sub), min(sub)


""" 
allr = []
with open("5313_all_pacbio.fastq") as infile:
    for line in infile:
        if line[0] in ['A','C','G','T','N']:
            allr.append(len(line))

print 'done 3'
print len(allr), np.median(allr), np.mean(allr), np.std(allr), max(allr), min(allr)
"""

fig, ax = plt.subplots(figsize=(12,5))
#ax1   = plt.subplot2grid((2, 2), (0, 0))
ax0   = plt.subplot2grid((2, 2), (0, 0),rowspan=2)
ax2   = plt.subplot2grid((2, 2), (0, 1),rowspan=2)


#allr = [2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,7000,8000,5000,5000,5000,5000,1000,45000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,5000,6000,1200,1200,1100,1100,1000,1150]
#sub = [2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,1000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,7000,8000,5000,5000,5000,5000,1000,45000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,5000,6000,1200,1200,1100,1100,1000,1150]
#long = [2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,7000,8000,5000,5000,5000,5000,1000,45000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,2000,3000,4000,5000,6000,1200,1200,1100,1100,1000,1150]
#ccs = [3000,4000,5000,3000,4000,5000,3000,3400,3400,6000,5500,5400,4500]


bp = ax0.boxplot([sub, long, ccs], [0,1,2],patch_artist=True,  widths = [0.5, 0.5,0.5],showfliers=True)

colors = ['b', 'g', 'r']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
for median in bp['medians']:
    median.set(color='w', linewidth=2)
#bp = ax1.boxplot([ sub, long, ccs], [0,1,2],patch_artist=True,  widths = [0.5, 0.5,0.5],showfliers=True)
#colors = ['b', 'g', 'r']
#for patch, color in zip(bp['boxes'], colors):
#    patch.set_facecolor(color)
#for median in bp['medians']:
#   median.set(color='w', linewidth=2)
ax0.set_ylim(0,115000)
#ax1.set_ylim(80000,120000)
#ax1.spines['right'].set_visible(False)
#ax1.spines['top'].set_visible(False)
#ax1.spines['bottom'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.spines['bottom'].set_visible(False)
#ax1.spines['left'].set_visible(False)
#ax1.spines['left'].set_visible(False)
#ax0.plot((0.5,0.5),(0,22300),'k-',linewidth=1.5, clip_on=False)
ax0.plot((0.5,0.5),(0,115000),'k-',linewidth=1.5,clip_on=False)
#ax0.plot((0.44,0.56),(22000,27000),'k-',linewidth=1.5,clip_on=False)
#ax0.plot((0.44,0.56),(23000,24000),'k-',linewidth=1.5,clip_on=False)
ax0.set_xticklabels(['Filtered reads','Long reads','CCS reads'])
#ax1.set_xticks([])


ax2.set_ylabel('# of reads')
ax0.set_ylabel('# of reads')

ax2.set_xlabel('Read length (bp)')

ax2.hist(long, bins=100, color = 'b', alpha=0.6)
ax2.hist(sub, bins=100, color = 'g', alpha=0.6)
ax2.hist(ccs, bins=100, color = 'r', alpha=0.6)
ax2.set_xlim(0,50000)
ax2.set_ylim(0,140000)

ax2.plot(35000,130000,marker = 's',markersize = 8,color = '#287566',alpha = 0.6)
ax2.plot(35000,110000,marker = 's',markersize = 8,color = '#66b266',alpha = 0.6)
ax2.plot(35000,90000,marker = 's',markersize = 8,color = '#a82e28',alpha = 0.6)
ax2.text(37000,130000,'Long reads',va='center')
ax2.text(37000,110000,'Filtered reads',va='center')
ax2.text(37000,90000,'CCS reads',va='center')
ax0.text(0.,115000,'A',fontsize=18)

ax2.text(-11000,140000,'B',fontsize=18)


plt.savefig('5313.png',dpi=600,  format='png')
