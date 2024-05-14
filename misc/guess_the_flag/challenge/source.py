import re

flag = "ingeneer{REDACTED}"

def check(input):
    global flag
    if re.search(input, flag) == None:
        return "nope"
    else:
        return "nope"
    
print(check(input('guess the flag pls:')))

