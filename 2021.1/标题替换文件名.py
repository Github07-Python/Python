# -*- coding: utf-8 -*-
"""
NameChange1.0
This is a program that automatically modifies
 the name of an word document.

 author:fanghao
"""
from docx import Document
import os


# 这个是放所有待修改的word文件的目录
dir_1 = "F:\\a"                           #C:\\Users\\visg\\Desktop\\4
filenames = os.listdir(dir_1)

# 自动修改
for a in range(len(filenames)):
    print(filenames[a])
    dir_docx = dir_1 + "\\" + filenames[a]
    try:
        document = Document(dir_docx)
    except:
        print("error")
    else:
        new_name = document.paragraphs[0].text + '.docx'
        try:
            os.rename(dir_1 + os.sep + filenames[a], dir_1 + os.sep + new_name)
        except(FileNotFoundError, FileExistsError, OSError):
            print("FileNotFoundError")
