import re
import string

def rege(i):
    return i.group(1) + i.group(2).upper()

s = "hi,  hello world!"
jap = "hi 10a 有限公司"
res = re.sub("(^|\\s)(\\S)", rege, jap)
print(res)

#using capwords
res_cap = string.capwords(s)
print(res_cap)
