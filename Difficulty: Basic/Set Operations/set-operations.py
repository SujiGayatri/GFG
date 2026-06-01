def setInsert(arr, n):
    #code here
    s = set(arr)
    return s

def setDisplay(s):
    #code here
    for x in sorted(s):
        print(x, end=" ")
    print()

def setErase(s, x):
    #code here
    if x in s:
        s.remove(x)
        print("erased", x)
    else:
        print("not found")
