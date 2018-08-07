# -*- coding:utf-8*-
import importlib,sys
importlib.reload(sys)

import os
import os.path


##########################合并同一个文件夹下多个txt################
def MergeTxt(filepath,outfile):
    k = open(filepath+outfile, 'w+', encoding='utf8')
    # k = open(filepath+outfile, 'a+', encoding='gb18030',errors='ignore')
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)  # txtpath就是所有文件夹的路径
            f = open(txtPath, encoding="utf8")
            ##########换行写入##################
            for line in f.readlines():
                k.writelines(line)
    k.close()

    ##########################逐行读取文件分开放到两个文件里################
def divisionTxt():
    # 打开文件
    f = open('all.txt', 'r', encoding="utf8")
    answer = open('answer.txt', 'w', encoding="utf8")
    question = open('question.txt', 'w', encoding="utf8")
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        if i % 2 == 0:
            answer.write(line )
        else:
            question.write(line)


if __name__ == '__main__':
    # filepath="E:/code/chinese/"
    # outfile="all.txt"
    # MergeTxt(filepath,outfile)
    divisionTxt()
    print("haole")