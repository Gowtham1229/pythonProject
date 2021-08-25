
pos = -1                    # pos stands for position
def search(list, n):

    for i in range(len(list)):
        if list[i]==n:
           globals()['pos']= i
           return True
    return False

list = [1, 2, 5, 7, 9, 6, 7]

n = 10

if search(list, n):
    print("found",pos + 1)
else:
    print("not found")


