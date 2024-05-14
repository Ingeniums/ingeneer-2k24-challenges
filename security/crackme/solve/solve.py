#!/usr/bin/env python3
key = "GhOrsgInPJFpJ78gOw8erLmbXWPAoj"
key = "GhOr2gInPJFpJXYgO6YerLmbxwPAoj"


def decrypt(s, num):
    arr = list(s)
    for i in range(len(arr)):
        if arr[i].isalpha():
            if arr[i].islower():
                if ord(arr[i]) < (ord("a") + num):
                    arr[i] = chr(ord("Z") + 1 + (ord(arr[i]) - ord("a")) - num)
                else:
                    arr[i] = chr(ord(arr[i]) - num)
            elif arr[i].isupper():
                if ord(arr[i]) < (ord("A") + num):
                    arr[i] = chr(ord("9") + 1 + (ord(arr[i]) - ord("A")) - num)
                else:
                    arr[i] = chr(ord(arr[i]) - num)
        elif arr[i].isdigit():
            if ord(arr[i]) < (ord("0") + num):
                arr[i] = chr(ord("z") + 1 + (ord(arr[i]) - ord("0")) - num)
            else:
                arr[i] = chr(ord(arr[i]) - num)
        
    return "".join(arr)
    
# Z -> a
# z -> 0
# 9 -> A

print(decrypt("OpWz0oQvXRNxRFGoW4GmzTujfeXIwr", 8))