import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from statistics import mean

cpath = os.getcwd()

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        #print eachNum
        for futherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = cpath +'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFile)


def threshold (imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)
    
    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3])> balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
        return newAr

i = Image.open(cpath+ '\\images\\numbers\\0.1.png')
iar = np.array(i)
i2 = Image.open(cpath + '\\images\\numbers\\y0.4.png')
iar2 = np.array(i2)
i3 = Image.open(cpath + '\\images\\numbers\\y0.5.png')
iar3 = np.array(i3)
i4 = Image.open(cpath + '\\images\\sentdex.png')
iar4 = np.array(i4)

iar = threshold(iar)
iar2 = threshold(iar2)
iar3 = threshold(iar3)
iar4 = threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()


#i = Image.open('pic2.jpg')
#iar = np.asarray(i)

#plt.imshow(iar)
#plt.show()

#print (iar)
#print (len(iar))
