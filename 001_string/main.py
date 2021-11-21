#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: lei.si
# Date: 2021年11月20日
# Description: string 常见字符串操作

import string
import datetime


class FormatValue(object):
    def __init__(self, string):
        self.string = string


if __name__ == '__main__':
    # 按照位置 index 打印
    print("{0} {1} {0}".format('全栈笔记本', 'Python 核心编程'))

    # string.format 格式化字符串的用法，其实内部调用了 vformat 包装器
    print("Chinese:{chinese}, English:{english}".format(english="core-programming", chinese="核心编程"))

    # 上述可以修改为通过字典设置 format 下的参数
    dist = {"english": "core-programming", "chinese": "核心编程"}
    # 此处注意 dist 前需要加上两个“星号” 用于取 value, 同理一个“星号”用于取 key
    print("Chinese:{chinese}, English:{english}".format(**dist))

    # format 也可以传入对象
    format_value = FormatValue("核心编程 面试解析")
    print('全栈笔记本 Python {0.string}'.format(format_value))

    # 循环遍历 string 并返回一个可迭代的 tuple 元组
    str_tmp = "全栈笔记本 Python {核心编程} {面试:详解}"
    str_tuple = string.Formatter().parse(str_tmp)
    for i, v in enumerate(str_tuple):
        print(i, v)

    # 左对齐文本以及指定宽度
    print('{:<30}'.format('全栈笔记本 Python 核心编程'))
    # 右对齐文本以及指定宽度
    print('{:>30}'.format('全栈笔记本 Python 核心编程'))
    # 中央对齐文本以及指定宽度
    print('{:^30}'.format('全栈笔记本 Python 核心编程'))
    # 中间齐文本并填充以及指定宽度
    print('{:*^30}'.format('全栈笔记本 Python 核心编程'))

    # 使用逗号作为千位分隔符
    print('{:,}'.format(1234567890))

    # 表示百分数，最后一位四舍五入
    print('全栈笔记本 Python, 输出百分数: {:.4%}'.format(2 / 3))

    # 时间日期格式化
    date = datetime.datetime(2021, 11, 20, 23, 9, 58)
    print('{:%Y-%m-%d %H:%M:%S}'.format(date))

    # 拆分字符串中的英语单词，按照空格开分割
    print(str.split('全栈笔记本 Python core programming'))

    # 将字符串转为首字母大写
    print(str.capitalize('python core programming'))

    # 截取字符串
    str1 = '全栈笔记本'
    str2 = "Python core programming"
    print("str1[0]: ", str1[0])
    print("str2[1:5]: ", str2[3:7])

    # 拼接字符串
    str1 = '全栈笔记本 '
    str2 = "Python core programming"
    print(str1 + str2)

    # 重复输出字符串
    str1 = 'python core programming '
    print(str1*2)

    # 计算字符串出现次数
    str1 = "全栈笔记本 Python core programming"
    str2 = 'm'
    print("str1.count('m') : ", str1.count(str2))

    # 字符串编解码
    str1 = "全栈笔记本 Python core programming"
    str1_utf8 = str1.encode("UTF-8")
    str1_gbk = str1.encode("GBK")

    print(str1)

    print("UTF-8 编码：", str1_utf8)
    print("GBK 编码：", str1_gbk)

    print("UTF-8 解码：", str1_utf8.decode('UTF-8', 'strict'))
    print("GBK 解码：", str1_gbk.decode('GBK', 'strict'))

    # endswith 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False
    str1 = '全栈笔记本 Python core programming!!'
    str1_end_flag = '!!'
    print(str1.endswith(str1_end_flag))
    print(str1.endswith(str1_end_flag, 20))
    print(str1.endswith(str1_end_flag, 0, 10))

    # expandtabs 方法把 \t 转换为指定空格，默认为8
    str1 = '全栈笔记本\tPython\tcore\tprogramming!!'
    print('使用 6 个空格:', str1.expandtabs(4))

    # find 方法查找字符串中指定子串，成功返回 index 位置，失败返回 -1
    search_str = '全栈笔记本 Python core programming!!'
    target_str = '!!'
    print(search_str.find(target_str))
    print(search_str.find(target_str, 20))
    print(search_str.find(target_str, 0, 10))

    # index 方法查找字符串中指定子串，成功返回 index 位置，失败返回 -1
    # 与 find 的区别为如果没有找到则报错
    search_str = '全栈笔记本 Python core programming!!'
    target_str = '!!'
    print(search_str.index(target_str))
    print(search_str.index(target_str, 20))
    # print(search_str.index(target_str, 0, 10))

    # isalnum 方法检测字符串是否由字母和数字组成
    str1 = '全栈笔记本 Python core programming'
    print(str1.isalnum())
    str1 = '1Python2core3programming'
    print(str1.isalnum())

    # isalpha 方法检测字符串是否只由字母或文字组成
    str1 = '全栈笔记本Python'
    print(str1.isalpha())
    str1 = '1Python2core3programming'
    print(str1.isalpha())

    # isdigit 方法检测字符串是否只由数字组成
    str1 = '全栈笔记本Python'
    print(str1.isdigit())
    str1 = '123'
    print(str1.isdigit())

    # islower 方法检测字符串是否由小写字母组成
    str1 = '全栈笔记本Python'
    print(str1.islower())
    str1 = '全栈笔记本python'
    print(str1.islower())

    # isnumeric 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字
    str1 = '全栈笔记本Python123'
    print(str1.isnumeric())
    str1 = '123'
    print(str1.isnumeric())

    # isspace 方法检测字符串是否只由空白字符组成
    str1 = ' '
    print(str1.isspace())
    str1 = '全栈笔记本 Python'
    print(str1.isspace())

    # istitle 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
    str1 = '全栈笔记本 Python Core Programming'
    print(str1.istitle())
    str1 = '全栈笔记本 Python core programming'
    print(str1.istitle())

    # title 方法返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写
    str1 = 'python core programming'
    print(str1.title())

    # isupper 方法检测字符串中所有的字母是否都为大写
    str1 = '全栈笔记本 Python Core Programming'
    print(str1.isupper())
    str1 = '全栈笔记本 PYTHON CORE PROGRAMMING'
    print(str1.isupper())

    # upper 方法将字符串中的小写字母转为大写字母
    str1 = 'python core programming'
    print(str1.upper())

    # join 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
    str1 = '-'
    str2 = '全栈笔记本 Python Core Programming'
    print(str1.join(str2))

    # len 方法返回对象（字符、列表、元组等）长度或项目个数
    str1 = '全栈笔记本 Python Core Programming'
    print(len(str1))

    # ljust 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
    # rjust 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
    str1 = '全栈笔记本 Python Core Programming'
    print(str1.ljust(50, '*'))
    print(str1.rjust(50, '*'))

    # lower 方法转换字符串中所有大写字符为小写
    str1 = '全栈笔记本 PYTHON CORE PROGRAMMING'
    print(str1.lower())

    # lstrip 方法用于截掉字符串左边的空格或指定字符
    str1 = '          全栈笔记本 python core programming'
    print(str1.lstrip())

    # max 方法返回字符串中最大的字母
    # min 方法返回字符串中最小的字母
    str1 = 'python core programming'
    print(max(str1))
    print(min(str1))

    # replace 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
    str1 = '全栈笔记本 python core programming'
    print(str1.replace("python", "cpp", 3))

    # rfind 返回字符串最后一次出现的位置，如果没有匹配项则返回-1
    str1 = '全栈笔记本 python core programming'
    print(str1.rfind("python"))

    # rindex 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间
    str1 = '全栈笔记本 python core programming'
    print(str1.rindex("python"))

    # rstrip 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符
    str1 = '全栈笔记本 python core programming\t'
    print(str1.rstrip())

    # split 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串
    str1 = '全栈笔记本 python core programming'
    print(str1.split(" "))

    # splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符
    str1 = '全栈笔记本\rpython\ncore\tprogramming'
    print(str1.splitlines())

    # startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查
    str1 = 'python core programming'
    print(str1.startswith("python"))

    # strip 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列
    str1 = 'python core programming'
    print(str1.strip("python"))

    # swapcase 方法用于对字符串的大小写字母进行转换，即将大写字母转换为小写字母，小写字母会转换为大写字母
    str1 = 'python core PROGRAMMING'
    print(str1.swapcase())

    # zfill 方法返回指定长度的字符串，原字符串右对齐，前面填充0
    str1 = 'python core programming'
    print(str1.zfill(50))

    # isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象
    str1 = 'python core programming'
    print(str1.isdecimal())
    str1 = '0123456789'
    print(str1.isdecimal())
