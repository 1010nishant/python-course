position = -1


def search(list, element):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2

        if list(mid) == element:
            globals()['position'] = mid
            return True
        else:
            if list(mid) < element:
                l = mid + 1
            else:
                u = mid - 1
    return False


# in binary search we have the sorted list or array


list = [1, 3, 4, 5, 6, 23, 47, 78, 83, 98]
element = 23

if search(list, element):
    print("found at ", position+1)
else:
    print("not found")
