# https://www.careercup.com/question?id=6185570560638976

def lexiSort(num):
    sortedlst = []
    if num <= 9:
        for i in range(1, num+1):
            sortedlst.append(i)
        return sortedlst

    maxsingledigit = 9
    for i in range(1, 10):
        sortedlst.append(i)
        pass




if __name__ == "__main__":
    lexiSort(30)