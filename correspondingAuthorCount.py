import pandas as pd
from xpinyin import Pinyin
import numpy as np
import os
import re

def transPinyin(s):
    p = Pinyin()
    result = p.get_pinyin(s)
    s = result.split('-')
    result = s[0].lower() + ''.join(s[1:]).lower()
    # print(result)
    return result

def fun(string):
    if string != None:
        searchObj = re.search(r';*.*\(', string ,re.I)
        left = searchObj.start()
        right = searchObj.end()
        string = string[left:right-1]

        authorName = string.split(';')[-1]

        result = authorName.split(',')
        result = result[0] + ''.join(result[1:])
        result = result.split(' ')
        result = result[0] + ''.join(result[1:])
        return result
def transformName(string):
    result = string.split(',')
    result = result[0] + ''.join(result[1:])

    result = result.split(' ')
    result = result[0] + ''.join(result[1:])

    return result

def countBiger(string):
    res = ""
    count = 0
    for i in string:
        if(i >= 'A' and i <= 'Z'):
            res += i
            count += 1
        if count > 1:
            break
    return res

def cmp(string1, string2):
    res1 = countBiger(string1)
    res2 = countBiger(string2)
    return res1 == res2

if __name__ == "__main__":
    names = pd.read_excel('names.xlsx')
    list = pd.read_excel('list.xlsx')

    chineseNames = names['姓名'].values
    authorAddress = list['通讯作者地址'].values
    print("初始时，通讯作者地址的个数：",len(authorAddress))
    allAuthors = list['全部作者'].values

    # 得到所有通讯作者的缩写
    authorAddressResult = []
    for string in authorAddress:
        authorAddressResult.append(fun(string))
    print("通讯作者缩写的个数：",len(authorAddressResult))

    #存储通讯作者的全拼
    FinallResult = []
    # i 作为计时器遍历通讯作者得到全拼
    i = 0
    for item in allAuthors:
        list = item.split('|')
        transformNameList = []
        for a in list:
            a = transformName(a)
            transformNameList.append(a)
        # print(i, transformNameList)
        flag = 0
        for value in transformNameList:
            res1 = countBiger(authorAddressResult[i])
            res2 = countBiger(value)
            if(cmp(res1,res2)):
                FinallResult.append(value)
                flag = 1
                break
        if(flag == 0):
            FinallResult.append("None")
        i += 1
    print(FinallResult)
    #得到了通讯作者的全拼
    print("通讯作者的个数（测试1）：",len(FinallResult))

    test1 = pd.DataFrame({'test': FinallResult,})
    test1.to_excel("test.xlsx", index=False)

    #   ----------------------------
    #      通讯作者拼音转为姓名
    #   ----------------------------
    ChineseNames = names['姓名'].values
    PinyinNames = []
    for s in ChineseNames:
        value = transPinyin(s)
        # print(value)
        value.lower()
        PinyinNames.append(value)
    dictionary = dict(zip(PinyinNames, ChineseNames))
    print('拼音对应中文姓名字典:', dictionary)

    correspondingAuthorPinyin = []
    for s in FinallResult:
        s = s.split(',')
        result = s[0].lower() + ''.join(s[1:]).lower()

        s = result.split(' ')
        result = s[0].lower() + ''.join(s[1:]).lower()

        s = result.split('-')
        result = s[0].lower() + ''.join(s[1:]).lower()

        correspondingAuthorPinyin.append(result)

    print('通讯作者的拼音总个数:', len(correspondingAuthorPinyin))

    ChineseArray = []
    for ss in correspondingAuthorPinyin:
        # ss.lower()
        ChineseArray.append(dictionary.get(ss, 'None'))
    # print(ChineseArray)
    numbers = ChineseArray.count('None')
    print('总长度:', len(ChineseArray))
    print('未找到的数量:', numbers)

    result = pd.DataFrame({'通讯作者拼音': correspondingAuthorPinyin,
                           '通讯作者名字': ChineseArray, })
    result.to_excel("correspondingAuthorName.xlsx",index=False)