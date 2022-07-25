position = -1

def search(list, element):
    i = 0

    # while i < len(list):
    for i in list:
        if list[i] == element:
            globals() ['position'] = i
            # print("found here")
            return True
        # i= i+1
    return False


list = [1, 3, 5, 6, 4, 3, 23, 5, 4, 56, 78, 9, 83, 47]
element = 23

if search(list,element):
    print("found at ", position+1)
else:
    print("not found")