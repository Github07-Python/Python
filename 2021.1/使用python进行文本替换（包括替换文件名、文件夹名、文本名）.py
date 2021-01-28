#https://blog.csdn.net/qq_40705355/article/details/85337864?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

import os
import chardet

from time import clock

def timer(f):

    def _f(*args):

        t0 = clock()

        f(*args)

        return clock() - t0

    return _f


class replace:
    path = ""
    dict_repalce = {}
    tuple_notreplace = ()

    def __init__(self, p, d, t):
        self.path = p
        self.dict_replace = d
        self.tuple_notreplace = t

    def replace(self):
        if os.path.isdir(self.path):  # 判断是否是一个文件夹
            li_os = os.listdir(self.path)  # 返回一个文件节的列表
            for every_dir in li_os:  # 循环判断每一个是否是文件夹
                filePath = os.path.join(self.path, every_dir)
                if os.path.isdir(filePath):  # 如果是一个文件夹
                    print(filePath, "这是一个文件夹")
                    filename = os.path.basename(filePath)
                    bool_change = False  # 判断文件名是否更改的标志
                    for key in self.dict_replace.keys():  # 循环查看key
                        if key in filename:  # 查看key是不是存在文件名的一部分
                            filename_new = filename.replace(key, self.dict_replace[key])
                            bool_change = True  # 文件名被更改
                    if bool_change == True:  # 判断文件名是否被修改
                        print(filename, "正在修改文件夹名。。。")
                        os.chdir(os.path.dirname(filePath))  # 修改工作路径
                        os.rename(os.path.basename(filePath), filename_new)  # 修改文件名
                        filePath = os.path.abspath(filename_new)
                        print(filename_new, "文件夹名修改成功。。。")
                    replace(filePath, self.dict_replace, self.tuple_notreplace).replace()

                else:
                    print(filePath, "这是一个文件")
                    filename = os.path.basename(filePath)
                    filename_li = filename.split('.')  # 分割，防止在修改文件名的时候把文件格式后缀一起修改了
                    bool_change = False  # 判断文件名是否更改的标志
                    for key in self.dict_replace.keys():  # 循环查看key
                        if key in filename_li[0]:  # 查看key是不是存在文件名的一部分
                            filename_li[0] = filename_li[0].replace(key, self.dict_replace[key])
                            bool_change = True  # 文件名被更改
                    if bool_change == True:  # 判断文件名是否被修改
                        filename_new = '.'.join(filename_li)  # 连接名称
                        print(filename, "正在修改文件名。。。")
                        os.chdir(os.path.dirname(filePath))  # 修改工作路径
                        os.rename(os.path.basename(filePath), filename_new)  # 修改文件名
                        filePath = os.path.abspath(filename_new)
                        print(filename_new, "文件名修改成功。。。")

                    for notreplace in self.tuple_notreplace:  # 循环不能更改内容的元组
                        if os.path.basename(filePath).endswith(notreplace):  # 判断是不是不能更改类型的文件
                            print("文件内容没有修改。。。。")
                            break
                    else:
                        print("文件内容正在修改。。。。")
                        code = chardet.detect(open(filePath, 'rb').read())['encoding']  # 获取文件编码
                        print('编码格式', code)
                        with open(filePath, errors='ignore', encoding=code) as f:  # 以自己的编码格式打开文件
                            file_str = f.read()
                        for key in self.dict_replace.keys():  # 循环查看key
                            if key in file_str:  # 查看key是不是存在文件名的一部分
                                file_str = file_str.replace(key, self.dict_replace[key])
                        with open(filePath, 'w', encoding=code) as f:
                            f.write(file_str)
                            print("文件内容修改完成。。。。")


        elif os.path.isfile(self.path):  # 判断是不是一个文件
            filename = os.path.basename(self.path)
            filename_li = filename.split('.')  # 分割，防止在修改文件名的时候把文件格式后缀一起修改了
            bool_change = False  # 判断文件名是否更改的标志
            for key in self.dict_replace.keys():  # 循环查看key
                if key in filename_li[0]:  # 查看key是不是存在文件名的一部分
                    filename_li[0] = filename_li[0].replace(key, self.dict_replace[key])
                    bool_change = True  # 文件名被更改
            if bool_change == True:  # 判断文件名是否被修改
                filename = '.'.join(filename_li)
                print(filename, "正在修改文件名。。。")
                os.chdir(os.path.dirname(self.path))  # 修改工作路径
                os.rename(os.path.basename(self.path), filename)  # 修改文件名
                self.path = os.path.abspath(filename)
                print(filename, "修改成功文件名成功。。。")

            for notreplace in self.tuple_notreplace:  # 循环不能更改内容的元组
                if os.path.basename(self.path).endswith(notreplace):  # 判断是不是不能更改类型的文件
                    print("文件内容没有修改。。。。")
                    break
            else:
                print("文件内容正在修改。。。。")
                code = chardet.detect(open(filePath, 'rb').read())['encoding']
                with open(self.path, encoding=code) as f:
                    file_str = f.read()
                for key in self.dict_replace.keys():  # 循环查看key
                    if key in file_str:  # 查看key是不是存在文件名的一部分
                        file_str = file_str.replace(key, self.dict_replace[key])
                with open(self.path, 'w', encoding=code) as f:
                    f.write(file_str)
                    print("文件内容修改完成。。。。")


if __name__ == "__main__":
    path = "D:\TestABCabc 1\wwwroot"
    dict_replace = {'a': "ZQQ", 'c': 'GG'}  # 需要替换字符串的字典
    tuple_notreplace = ('.png', '.pptx', '.xlsx', '.docx', 'jpg', 'psd', '.eot', '.ttf', '.gif')  # 不替换内容的元组
    re = replace(path, dict_replace, tuple_notreplace)
    start = time.clock()
    print(start)
    re.replace()
    end = time.clock()
    print(end)
    print("程序运行时间：", end - start)

#原文链接：https: // blog.csdn.net / qq_40705355 / article / details / 85337864