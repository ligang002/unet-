from __future__ import division
from unet2d.model_GlandCeil import unet2dModule
import numpy as np
import pandas as pd
import cv2
import os


def train():
    # Read  data set (Train data from CSV file)
    csvmaskdata = pd.read_csv('./GlandsMask.csv')
    csvimagedata = pd.read_csv('./GlandsImage.csv')
    # imagedata:二维列表
    maskdata = csvmaskdata.iloc[:, :].values
    imagedata = csvimagedata.iloc[:, :].values
    # 把训练集打乱顺序
    perm = np.arange(len(csvimagedata))
    np.random.shuffle(perm)
    imagedata = imagedata[perm]
    maskdata = maskdata[perm]
    # 图片大小为 720 * 720
    unet2d = unet2dModule(720, 720, channels=3, costname="dice coefficient")
    # 保存名称："./model/unet2dglandceil605.pd"
    # 日志："./log"
    # 学习率：0.0005
    # drop_out：1
    # 次数：40000
    # batch_size： 2
    unet2d.train(imagedata, maskdata, "./model/unet2dglandceil605.pd",
                 "./log", 0.0005, 1, 40000, 2)


def predict():
    fromImageDir = "./JPEGImages/"
    # 输出文件的保存位置
    toImageDir = "./JR-604/"
    unet2d = unet2dModule(720, 720, 3)
    filelist = os.listdir(fromImageDir)  # 该文件夹下所有的文件（包括文件夹
    for file in filelist:  # 遍历所有文件
        if file < '000000':
            continue
        else:
            Olddir = os.path.join(fromImageDir, file)  # 原来的文件路径
            if os.path.isdir(Olddir):  # 如果是文件夹则跳过
                continue
            true_img = cv2.imread(Olddir, cv2.IMREAD_COLOR)
            test_images = true_img.astype(np.float)

            test_images = np.multiply(test_images, 1.0 / 255.0)

            # predictvalue = unet2d.prediction("C:\\Users\\admin\\Desktop\\GlandCeil_Unet\\model\\unet2dglandceil27.pd",
            #                                  test_images)
            predictvalue = unet2d.prediction(".\\model\\unet2dglandceil604.pd",
                                             test_images)
            cv2.imwrite(toImageDir + '/' + file, predictvalue)


def main(argv):
    if argv == 1:
        train()
    if argv == 2:
        predict()


if __name__ == "__main__":
    main(1)
