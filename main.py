import pandas as pd
from xpinyin import Pinyin
import numpy as np
import os

names = pd.read_excel('names.xlsx')
list = pd.read_excel('list.xlsx')
ChineseNames = names['姓名'].values

def transPinyin(s):
    p = Pinyin()
    result = p.get_pinyin(s)
    s = result.split('-')
    result = s[0].lower() + ''.join(s[1:]).lower()
    # print(result)
    return result


PinyinNames = []
for s in ChineseNames:
    value = transPinyin(s)
    # print(value)
    value.lower()
    PinyinNames.append(value)

# print(ChineseNames)
# print(PinyinNames)
dictionary = dict(zip(PinyinNames,ChineseNames))
print('拼音对应中文姓名字典:', dictionary)


firstAuthor = list['一作'].values
# print("firstAuthor:", firstAuthor)

firstAuthorPinyin = []
for s in firstAuthor:
    s = s.split(',')
    result = s[0].lower() + ''.join(s[1:]).lower()

    s = result.split(' ')
    result = s[0].lower() + ''.join(s[1:]).lower()

    s = result.split('-')
    result = s[0].lower() + ''.join(s[1:]).lower()

    # result = result.split(' ')
    firstAuthorPinyin.append(result)
print('第一作者的拼音:', firstAuthorPinyin)
print('第一作者的拼音总个数:', len(firstAuthorPinyin))

ChineseArray = []
for ss in firstAuthorPinyin:
    # ss.lower()
    ChineseArray.append(dictionary.get(ss, 'None'))
print(ChineseArray)
numbers = ChineseArray.count('None')
print('总长度:',len(ChineseArray))
print('未找到的数量:',numbers)


# # df=pd.DataFrame(ChineseNames)
# list["一作姓名（老师）"] = ChineseNames
# list.to_excel('result.xlsx')

result  = pd.DataFrame({'拼音':list['一作'].values,
                        '一作名字':ChineseArray,})
result.to_excel("result.xlsx")