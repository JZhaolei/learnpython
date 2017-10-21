import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D #3D必需的模块，project = '3d'的定义

np.random.seed(42)
n_grids = 51 #x-y平面的格点数
c = n_grids/2 #中心位置
nf = 2 #低频成分个数
x = np.linspace(0,1,n_grids) # 长度为n_grids的array
y = np.linspace(0,1,n_grids)
X,Y = np.meshgrid(x,y) #把x,y组合成n_grids*n_grids的array,X，Y为格点坐标
spectrum = np.zeros((n_grids,n_grids), dtype = np.complex)#生成一个0值的傅立叶谱
noise = [np.complex(x,y) for x,y in np.random.uniform(-1,1,((2*nf+1)**2/2,2))]#生成一段噪音，长度为2*nf+1)**2/2
noisy_block = np.concatenate((noise,[0j],np.conjugate(noise[::-1])))#傅立叶频谱的每一项和其共轭关于中心对称
spectrum[c-nf:c+nf+1, c-nf:c+nf+1] = noisy_block.reshape((2*nf+1, 2*nf+1))#将生成的频谱作为低频成分
Z = np.real(np.fft.ifft2(np.fft.ifftshift(spectrum)))#反傅立叶变换
fig = plt.figure('3D surface & wire')#surface图
ax = fig.add_subplot(1,2,1, projection = '3d')
ax.plot_surface(X,Y,Z, alpha = 0.7, cmap = 'jet', rstride = 1, cstride = 1, lw=0)#lpha是透明度，retride和cstride是两个方向的采样，越小越精细，lw是线宽
ax = fig.add_subplot(1,2,2,projection = '3d')
ax.plot_wireframe(X,Y,Z,rstride = 3, cstride =3, lw=0.5)#网线图
plt.show() 
