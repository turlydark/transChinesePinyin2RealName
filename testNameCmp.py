string1 = 'ZhouGGGGG'
string2 = ['ZhousaddasgGen','ZfdfDf',"ZGgen"]
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
for i in string2:
    if(cmp(string1,i)):
        print(i)
# print(cmp(string1,string2))