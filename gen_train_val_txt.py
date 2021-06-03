"""
根据一定文件夹结构下的图片，生成训练或检验所需的列表文件

Example train.txt:
/path/to/train/image1.png 0
/path/to/train/image2.png 1
/path/to/train/image3.png 2
/path/to/train/image4.png 0
.
.

@author: wgshun
"""

import os
import re
import shutil


def cut(x):
    x = x.split('_')
    n = ''
    for i in x[:-1]:
        n += '_' + i
    return n[1:]

def gen_val():
    image_path_test = 'data/补拍_test'
    label_dic ={}

    with open(os.path.join(image_path_test, 'val.txt'), 'w') as txt1:
        files = os.listdir(image_path_test)
        for _, file in enumerate(files):
            label_dic[file] = file.split('-')[0]
        for file in files:
            if os.path.splitext(file)[-1] != '.txt':
                str2 = str(label_dic[file])[:-1]
                if len(str(label_dic[file]))==1:
                    str2 = str(0)
                wr_str = os.path.join(image_path_test + '/', file) + ' ' + str2 + "\n"
                txt1.write(wr_str)
    txt1.close()

def gen_train():
    image_path = 'data/补拍1000'
    label_dic = {}
    with open(os.path.join(image_path, 'train.txt'), 'w') as txt:
        files = os.listdir(image_path)
        for _, file in enumerate(files):
            label_dic[file] = file.split('-')[0]
        for file in files:
            if os.path.splitext(file)[-1] != '.txt':
                str2 = str(label_dic[file])[:-1]
                if len(str(label_dic[file]))==1:
                    str2 = str(0)
                wr_str = os.path.join(image_path+'/', file) + ' ' + str2 + "\n"
                txt.write(wr_str)
    txt.close()

def file_mv():
    image_path = 'data/补拍1000'
    image_path_test = 'data/补拍_test'
    label_dic = {}
    files = os.listdir(image_path)
    for file in files:
        if os.path.splitext(file)[-1] != '.txt':
            if file.split('-')[1] == '93.png':
                shutil.move(os.path.join(image_path+'/', file), os.path.join(image_path_test+'/', file))

def file_mv2():
    image_path = 'data/黑底试纸'
    image_path_test = 'data/补拍1000'
    label_dic = {}
    files = os.listdir(image_path)
    for file in files:
        if os.path.splitext(file)[-1] != '.txt':
            # if file.split('-')[1] == '94.png':

            file1 = file.split('-')
            file2 = file1[1].split('.')
            file3 = int(file2[0])+100
            file4 = file1[0]+'-'+str(file3)+'.'+file2[1]
            shutil.move(os.path.join(image_path+'/', file), os.path.join(image_path_test+'/', file4))


def corr():
    with open('data/simpsons_dataset/train.txt', 'r+')as fp:
        dict = {}
        for line1 in fp.readlines():
            dict[line1.split('/')[-2]]=line1[-2]

    with open('data/kaggle_simpson_testset/val.txt','r+')as fb:
        with open('data/kaggle_simpson_testset/val1.txt','w+')as fb1:
            for line in fb.readlines():
                try:
                    label = dict[cut(line.split('/')[-1])]
                except KeyError:
                    continue
                line2 = line[:-2]+str(label)+'\n'
                fb1.writelines(line2)
# file_mv()
gen_val()
gen_train()