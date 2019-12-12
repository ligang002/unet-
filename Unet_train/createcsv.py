# author：lph
# funtion:image enhance
import os

fromImageDir = "./VOC2007/JPEGImages/"
toImageDir = "./VOC2007/grayImages/"

filelist = os.listdir(fromImageDir)  # 该文件夹下所有的文件（包括文件夹）
for file in filelist:  # 遍历所有文件
    filename = os.path.splitext(file)[0]  # 文件名
    filetype = os.path.splitext(file)[1]  # 文件扩展名
    f = open('GlandsImage.csv', 'a')
    # f.write('C:/Users/admin/Desktop/GlandCeil_Unet/VOC2007/JPEGImages/'+filename+filetype+'\n')
    f.write(r'E:\ligang\SVN\VOC2007\JPEGImages\\'+filename+filetype+'\n')
    f.close()

fileslist = os.listdir(toImageDir)  # 该文件夹下所有的文件（包括文件夹）
for files in fileslist:  # 遍历所有文件
    filename = os.path.splitext(files)[0]  # 文件名
    filetype = os.path.splitext(files)[1]  # 文件扩展名
    f1 = open('GlandsMask.csv', 'a')
    # f1.write('C:/Users/admin/Desktop/GlandCeil_Unet/VOC2007/grayImages/'+filename+filetype+'\n')
    f1.write(r'E:\ligang\SVN\VOC2007\grayImages\\'+filename+filetype+'\n')
    f1.close()