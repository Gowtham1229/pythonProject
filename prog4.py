pos = -1  # pos stands for position

def search(list, n):
    l = 0
    u = len(list) - l

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False

list = [1,2,5,7,9,56,789,897,1100]
n =897

if search(list,n):
     print("found",pos + 1)
else:
     print("not found")
