import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

t_hot = 304
t_cold = 14
ant = '3C'
nm = '20'


cold_l_ing = np.zeros((801), dtype=float)
cold_r_ing = np.zeros((801), dtype=float)
hot_l_ing = np.zeros((801), dtype=float)
hot_r_ing = np.zeros((801), dtype=float)





file=pd.read_csv(ant+'/X-pol/XH'+nm+'.csv', sep=',',skiprows=20,header=None)
file2=pd.read_csv( ant+'/X-pol/XC'+nm+'.csv', sep=',',skiprows=20,header=None)
print (file.columns) #writes the simulated values in columns
freq_0= file.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
hot_X_db = file.values[range(file.shape[0] - 1), 1].astype(float)
cold_X_db = file2.values[range(file.shape[0] - 1), 1].astype(float)


hot_X= 10 ** (hot_X_db/10)
cold_X= 10 ** (cold_X_db/10)




file=pd.read_csv(ant+'/Y-pol/YC'+nm+'.csv', sep=',',skiprows=20,header=None)
file2=pd.read_csv(ant+'/Y-pol/YH'+nm+'.csv', sep=',',skiprows=20,header=None)
print (file.columns) #writes the simulated values in columns
freq_0= file.values[range(0, file.shape[0] - 1), 0].astype(float) / 1e9
cold_Y_db = file.values[range(file.shape[0] - 1), 1].astype(float)
hot_Y_db = file2.values[range(file.shape[0] - 1), 1].astype(float)


hot_Y= 10 ** (hot_Y_db / 10)
cold_Y= 10 ** (cold_Y_db / 10)



Y_X = np.divide(hot_X, cold_X)
Y_Y = np.divide(hot_Y, cold_Y)


plt.figure(1)
plt.subplot(211)
plt.title(ant+'\nY for X-pol')
plt.plot(freq_0,Y_X)
plt.xlim(0.1, 15)
plt.ylim(0, 16)
plt.ylabel('unit')
plt.grid(1)
plt.subplot(212)
plt.title('Y for Y-pol')
plt.plot(freq_0,Y_Y)
plt.xlim(0.1, 16)
plt.ylim(0, 15)
plt.ylabel('unit')
plt.xlabel('frequency in GHz')
plt.grid(1)
plt.savefig("Y-factor.pdf", bbox_inches="tight")


plt.figure(2)
plt.subplot(211)
plt.title(ant+'\n Cold for X-pol')
plt.plot(freq_0,cold_X_db)
plt.xlim(0.1, 15)
plt.ylim(-70, -20)
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.title('Hot for X-pol')
plt.plot(freq_0,hot_X_db)
plt.xlim(0.1, 15)
plt.ylim(-70, -20)
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("SpecX.pdf", bbox_inches="tight")

plt.figure(3)
plt.subplot(211)
plt.title(ant+' \nCold for Y-pol')
plt.plot(freq_0,cold_Y_db)
plt.xlim(0.1, 15)
plt.ylim(-70, -20)
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.subplot(212)
plt.title('Hot for Y-pol')
plt.plot(freq_0,hot_Y_db)
plt.xlim(0.1, 15)
plt.ylim(-70, -20)
plt.xlabel('frequency in GHz')
plt.ylabel('measurement value in dBm')
plt.grid(1)
plt.savefig("SpecY.pdf", bbox_inches="tight")

t_sys_X = np.divide((t_hot - t_cold * Y_X), (Y_X - 1))
t_sys_Y = np.divide((t_hot - t_cold * Y_Y), (Y_Y - 1))

fig=plt.figure(4)
plt.subplot(211)
plt.title(ant+'\n System Temperature for X-pol (UP) and Y-pol (DOWN)')
plt.plot(freq_0,t_sys_X)
plt.ylim(-100,400)
plt.xlim(0.1, 15)
#plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.grid(1)
#plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')

plt.subplot(212)
#plt.title('System Temperature for Y-pol')
plt.plot(freq_0,t_sys_Y)
plt.ylim(-100,400)
plt.xlim(0.1, 15)
#plt.xticks([0,100,200,300,400,500,600,700,801],[0,1.5,3,4.5,6,7.5,9,10.5,12])
plt.grid(1)
plt.xlabel('frequency in GHz')
plt.ylabel('temperature in K')
plt.savefig("Tsys.pdf")#, bbox_inches="tight"
plt.show()

plt.close()

