
pos = -1                    # pos stands for position
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list = [1, 2, 5, 7, 9, 6, 7]

n = 9

if search(list, n):
    print("found",pos + 1)
else:
    print("not found")


