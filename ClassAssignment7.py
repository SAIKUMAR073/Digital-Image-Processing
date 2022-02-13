import numpy as np
import cv2
import matplotlib.pyplot as plt

Image = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg',0)

Peak_SNR=10*np.log10((255*255)/(1/(225*225)*np.sum(Image)*np.sum(Image)))
print('Peak_SNR is: ',Peak_SNR)

def Convert_to_binary(num):
    binary_num = [int(i) for i in list('{0:0b}'.format(num))]
    for j in range(8 - len(binary_num)):
        binary_num.insert(0,0)        
    return binary_num
def Convert_to_decimal(listt):
    x = 0
    for i in range(8):
        x = x + int(listt[i])*(2**(7-i))
    return x
def discriminate_bit(bit,Image):
    z = np.zeros([225,225])
    for i in range(225):
        for j in range(225):
            x = Convert_to_binary(Image[i][j])
            for k in range(8):
                if k == bit:
                    x[k] = x[k]
                else:
                    x[k] = 0
            x1 = Convert_to_decimal(x)
            z[i][j] = x1
    return z
    # set up side-by-side image display
    
fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

for i in range(1,9):
    fig.add_subplot(4,2,i)
    plt.imshow(discriminate_bit(i-1,Image), cmap='gray')


plt.show(block=True)