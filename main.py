def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


def readfile():
    myArray = []
    fo = open("input.txt", "r")
    for line in fo:
        for nbr in line.split():
            myArray.append(int(nbr))
    return myArray


def writeToFile(arr):
    with open("output.txt", 'w') as file:
        for j in arr:
            file.write(str(j) + " ")


arrInput = readfile()
arrSort = quicksort(arrInput)
arrRes = []
for i in range(len(arrSort)):
    if arrInput[i] == arrSort[i]:
        arrRes.append(arrInput[i])
writeToFile(arrRes)
