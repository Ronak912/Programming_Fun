# https://www.careercup.com/question?id=5941866982801408


def findElement(arr, element, startidx, endidx):

    if arr[startidx] == element:
        return startidx

    if arr[endidx] == element:
        return endidx

    mididx = (startidx + endidx) / 2
    if arr[mididx] == element:
        return mididx
    print "midd: ", mididx, "==", arr[mididx]
    #if (arr[startidx] < element and arr[mididx] > element) or (arr[mididx] < element and arr[endidx] < element):
    #if (arr[startidx] < element and arr[mididx] > element) or (arr[startidx] > arr[endidx] and arr[endidx] < element and ):
    if arr[startidx] < element and (arr[mididx] > element or (arr[mididx] < element and arr[endidx] < element)):
    #if arr[startidx] < element and (arr[mididx] > element or arr[mididx] < element):
        return findElement(arr, element, startidx, mididx-1)
    else:
        return findElement(arr, element, mididx+1, endidx)

    return -1


if __name__ == '__main__':
    #                    M
    arr = [4, 6, 8, 14, -20, -9, -2, 0, 3]
    print findElement(arr, -9, 0, len(arr)-1)
    #                    M
    arr1 = [4, 6, 8, 14, 20, -9, -2, 0, 3]
    print findElement(arr1, -9, 0, len(arr1)-1)