'''Program to show Licght Curves of gamma-tay novae by showing stacked

graphs each with the same realtive scales'''



import numpy as np

import matplotlib.pylab as plt

import matplotlib as mat

import pandas as pd



import seaborn as sns

sns.set_style("whitegrid",
              {'axes.edgecolor': '.2',
               'axes.facecolor': 'white',
               'axes.grid': True,
               'axes.linewidth': 0.5,
               'figure.facecolor': 'white',
               'grid.color': '.8',
               'grid.linestyle': u'-',
               'legend.frameon': True,
               'xtick.color': '.15',
               'xtick.direction': u'in',
               'xtick.major.size': 3.0,
               'xtick.minor.size': 1.0,
               'ytick.color': '.15',
               'ytick.direction': u'in',
               'ytick.major.size': 3.0,
               'ytick.minor.size': 1.0,
               })

sns.set_context("poster")


#HFSS=pd.read_csv('OMT_006_2.csv', sep=',')
#file=pd.read_csv('S-Parameter-Pol-A.csv', sep=',')
file=pd.read_csv('V1_0.csv', sep=',')
print file.columns #writes the simulated values in columns
freq_e = file['Freq[GHz]'].values
S11_e = file['dB(St(Coax_D_X Coax_D_X))'].values
#S21_e = file['dB(St(Coax_D_X Arm_D_X))'].values
#S12_e = file['dB(St(Arm_D_X Coax_D_X))'].values
S22_e = file['dB(St(Coax_D_Y Coax_D_Y))'].values

file1=pd.read_csv('V3_0.csv', sep=',')
print file1.columns #writes the simulated values i
freq_1 = file1['Freq[GHz]'].values
S11_1 = file1['dB(St(Coax_D_X Coax_D_X))'].values
#S21_1 = file1['dB(St(Coax_D_X Arm_D_X))'].values
#S12_1 = file1['dB(St(Arm_D_X Coax_D_X))'].values
#S22_1 = file1['dB(St(Arm_D_X Arm_D_X))'].values

file2=pd.read_csv('V4_20.csv', sep=',')
print file2.columns #writes the simulated values
freq_2 = file2['Freq[GHz]'].values
S11_2 = file2['dB(St(Coax_D_X Coax_D_X))'].values
#S21_2 = file2['dB(St(Coax_D_X Arm_D_X))'].values
#S12_2 = file2['dB(St(Arm_D_X Coax_D_X))'].values
#S22_2 = file2['dB(St(Arm_D_X Arm_D_X))'].values

file3=pd.read_csv('V4_22.csv', sep=',')
print file3.columns #writes the simulated values
freq_3= file3['Freq[GHz]'].values
S11_3 = file3['dB(St(Coax_D_X Coax_D_X))'].values
#S21_3 = file3['dB(St(Coax_D_X Arm_D_X))'].values
#S12_3 = file3['dB(St(Arm_D_X Coax_D_X))'].values
S22_3 = file3['dB(St(Coax_D_Y Coax_D_Y))'].values





plt.figure()

plt.plot(freq_e, S11_e, linewidth=1.5,label='Return Loss Pol-X')
plt.plot(freq_e, S22_e, linewidth=1.5,label='Return Loss Pol-Y')

#plt.plot(freq_1, S11_1, linewidth=1.5,label='Return Loss V3_0')
#plt.plot(freq_1, S21_1, linewidth=1.5,label='Insertion Loss V.3')

#plt.plot(freq_2, S11_2, linewidth=1.5,label='Return Loss V2_20')
#plt.plot(freq_2, S21_2, linewidth=1.5,label='Insertion Loss V.3 Rogers 3006')

#plt.plot(freq_3, S11_3, linewidth=1.5,label='Return Loss V4_22')
#plt.plot(freq_2, S11_3, linewidth=1.5,label='Return Loss V4_10')


#plt.annotate('',
#            xy=(12.8, 3.135),  # theta, radius
#            xytext=(0.4, 0.67),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='black', shrink=0.06),
#            horizontalalignment='left',
#            verticalalignment='bottom',
#            fontsize=15
#            )


#plt.text(5.38, -4, 'LO @ 4.0 GHz and 14 dBm', fontsize=15,
#        bbox={'facecolor':'grey', 'alpha':0.2, 'pad':10})



plt.xlim(1, 15)
plt.ylim(-30,-0)
plt.ylabel('Magnitude (dB)')
plt.xlabel('Frequency (GHz)')

plt.grid(True)

plt.xticks([1,3,5,7,9,11,13,15])
#plt.yticks([-10,-15,-20,-25,-30])



plt.rcParams.update({'font.size': 12})



plt.plot((12, 12), (0, -90), 'k--',linewidth=2.0)
#plt.plot((15.4, 15.4), (0, -90), 'k--',linewidth=2.0)
#plt.plot((3, 9), (-15, -15), 'k:',linewidth=2.0)

legend = plt.legend(loc='best', shadow=True)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()  # all the text.Text instance in the legend
llines = leg.get_lines()  # all the lines.Line2D instance in the legend
plt.setp(ltext, fontsize='small')
plt.setp(llines, linewidth=1.5)      # the legend linewidth

plt.tight_layout()

plt.savefig('Comparison-Tip-Design.pdf', bbox_inches="tight")
#plt.savefig('returnloss.pdf')
plt.show()

