import re
import pandas as pd

list = pd.read_excel('list.xlsx')
names = pd.read_excel('names.xlsx')
chineseNames = names['姓名'].values
authorAddress = list['通讯作者地址'].values
allAuthors = list['全部作者'].values


word = "(corresponding author)"
string = "Zhou, GG (corresponding author), Zhejiang Southeast Space Frame CO LTD, Hangzhou 311209, Peoples R China."
string1 = "Wang, YH; Shen, SK (corresponding author), Yunnan Univ, Sch Life Sci, Kunming 2 Green Lake North Rd, Kunming 650091, Yunnan, Peoples R China."
string2 = "Bao, LX; Wang, JL (corresponding author), Yunnan Univ, Sch Chem Sci & Technol, Natl Demonstrat Ctr Expt Chem & Chem Engn Educ, Kunming 650091, Yunnan, Peoples R China."
def fun(string):
    if string != None:
        searchObj = re.search(r';*.*\(', string ,re.I)
        left = searchObj.start()
        # print("left is :",left)
        right = searchObj.end()
        # print("right is :",right)
        print(string[left:right-1])
        string = string[left:right-1]

        authorName = string.split(';')[-1]

        result = authorName.split(',')
        result = result[0] + ''.join(result[1:])
        result = result.split(' ')
        result = result[0] + ''.join(result[1:])
        return result
print(fun(string))

authors = allAuthors[0]
list = authors.split('|')
print(list)