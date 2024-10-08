import re

def passvalidate(list_of_pass):
    valid_passes=[]
    password_list = list_of_pass.split(',')
    for i in password_list:
        if (6<=len(i)<=12 and re.search(r'[a-z]',i) and re.search(r'[A-Z]',i) and re.search(r'[0-9]',i) and re.search(r'[$#@]',i)):
            valid_passes.append(i)

    return ','.join(valid_passes)
# ll="asqwr1234@1,aF145#,2w3E*,2We3345"
# print(passvalidate(ll))

